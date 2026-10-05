
from fastapi import FastAPI, HTTPException
from database import get_connection
from pydantic import BaseModel, Field


app = FastAPI(
    title="Mini E-commerce API",
    description="FastAPI + PostgreSQL E-commerce Backend",
    version="1.0.0"
)


# ============================================================
# PYDANTIC MODELS
# ============================================================

class CreateUser(BaseModel):
    name: str = Field(..., min_length=3)
    email: str = Field(..., min_length=3)


class ProductCreate(BaseModel):
    name: str = Field(..., min_length=3)
    description: str | None = None
    price: float = Field(..., gt=0)
    inventory: int = Field(..., ge=0)


class UpdateInventory(BaseModel):
    inventory: int = Field(..., ge=0)


class OrderItemCreate(BaseModel):
    product_id: int = Field(..., gt=0)
    quantity: int = Field(..., gt=0)


class OrderCreate(BaseModel):
    user_id: int = Field(..., gt=0)
    items: list[OrderItemCreate] = Field(..., min_length=1)


# ============================================================
# 1. CREATE USER
# ============================================================

@app.post("/users", status_code=201)
def create_user(user: CreateUser):

    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO users (name, email)
            VALUES (%s, %s)
            RETURNING id, name, email, created_at;
            """,
            (user.name, user.email)
        )

        new_user = cursor.fetchone()
        connection.commit()

        return {
            "id": new_user[0],
            "name": new_user[1],
            "email": new_user[2],
            "created_at": new_user[3]
        }

    except Exception as e:
        connection.rollback()

        if "duplicate key" in str(e).lower():
            raise HTTPException(
                status_code=400,
                detail="Email already exists"
            )

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

    finally:
        cursor.close()
        connection.close()


# ============================================================
# 2. CREATE PRODUCT
# ============================================================

@app.post("/products", status_code=201)
def create_product(product: ProductCreate):

    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO products
            (name, description, price, inventory)
            VALUES (%s, %s, %s, %s)
            RETURNING id, name, description, price, inventory, created_at;
            """,
            (
                product.name,
                product.description,
                product.price,
                product.inventory
            )
        )

        new_product = cursor.fetchone()
        connection.commit()

        return {
            "id": new_product[0],
            "name": new_product[1],
            "description": new_product[2],
            "price": float(new_product[3]),
            "inventory": new_product[4],
            "created_at": new_product[5]
        }

    except Exception as e:
        connection.rollback()

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

    finally:
        cursor.close()
        connection.close()


# ============================================================
# 3. VIEW PRODUCTS
# ============================================================

@app.get("/products")
def get_products():

    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(
            """
            SELECT
                id,
                name,
                description,
                price,
                inventory,
                created_at
            FROM products
            ORDER BY id;
            """
        )

        rows = cursor.fetchall()

        products = []

        for row in rows:
            products.append({
                "id": row[0],
                "name": row[1],
                "description": row[2],
                "price": float(row[3]),
                "inventory": row[4],
                "created_at": row[5]
            })

        return products

    finally:
        cursor.close()
        connection.close()


# ============================================================
# 4. UPDATE PRODUCT INVENTORY
# ============================================================

@app.patch("/products/{product_id}/inventory")
def update_inventory(
    product_id: int,
    inventory_data: UpdateInventory
):

    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(
            """
            UPDATE products
            SET inventory = %s
            WHERE id = %s
            RETURNING id, name, price, inventory;
            """,
            (
                inventory_data.inventory,
                product_id
            )
        )

        product = cursor.fetchone()

        if product is None:
            raise HTTPException(
                status_code=404,
                detail="Product not found"
            )

        connection.commit()

        return {
            "id": product[0],
            "name": product[1],
            "price": float(product[2]),
            "inventory": product[3]
        }

    except HTTPException:
        connection.rollback()
        raise

    except Exception as e:
        connection.rollback()

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

    finally:
        cursor.close()
        connection.close()


# ============================================================
# 5. CREATE ORDER
# ============================================================

@app.post("/orders", status_code=201)
def create_order(order: OrderCreate):

    connection = get_connection()
    cursor = connection.cursor()

    try:

        # ----------------------------------------------------
        # STEP 1: Check whether user exists
        # ----------------------------------------------------

        cursor.execute(
            """
            SELECT id
            FROM users
            WHERE id = %s;
            """,
            (order.user_id,)
        )

        user = cursor.fetchone()

        if user is None:
            raise HTTPException(
                status_code=404,
                detail="User not found"
            )


        # ----------------------------------------------------
        # STEP 2: Check all products and calculate total
        # ----------------------------------------------------

        order_total = 0
        order_items_data = []

        for item in order.items:

            cursor.execute(
                """
                SELECT
                    id,
                    name,
                    price,
                    inventory
                FROM products
                WHERE id = %s
                FOR UPDATE;
                """,
                (item.product_id,)
            )

            product = cursor.fetchone()

            if product is None:
                raise HTTPException(
                    status_code=404,
                    detail=f"Product {item.product_id} not found"
                )

            product_id = product[0]
            product_name = product[1]
            unit_price = product[2]
            inventory = product[3]


            # Check inventory

            if inventory < item.quantity:
                raise HTTPException(
                    status_code=400,
                    detail=(
                        f"Not enough inventory for "
                        f"{product_name}. Available: {inventory}"
                    )
                )


            # Calculate item total

            item_price = unit_price * item.quantity

            order_total += item_price


            # Store information temporarily

            order_items_data.append({
                "product_id": product_id,
                "product_name": product_name,
                "unit_price": unit_price,
                "quantity": item.quantity,
                "item_price": item_price
            })


        # ----------------------------------------------------
        # STEP 3: Create order
        # ----------------------------------------------------

        cursor.execute(
            """
            INSERT INTO orders
            (user_id, total_amount)
            VALUES (%s, %s)
            RETURNING id, status, created_at;
            """,
            (
                order.user_id,
                order_total
            )
        )

        new_order = cursor.fetchone()

        order_id = new_order[0]
        order_status = new_order[1]
        created_at = new_order[2]


        # ----------------------------------------------------
        # STEP 4: Insert order items + reduce inventory
        # ----------------------------------------------------

        response_items = []

        for item in order_items_data:

            cursor.execute(
                """
                INSERT INTO order_items
                (
                    order_id,
                    product_id,
                    unit_price,
                    quantity,
                    item_price
                )
                VALUES (%s, %s, %s, %s, %s);
                """,
                (
                    order_id,
                    item["product_id"],
                    item["unit_price"],
                    item["quantity"],
                    item["item_price"]
                )
            )


            # Reduce product inventory

            cursor.execute(
                """
                UPDATE products
                SET inventory = inventory - %s
                WHERE id = %s;
                """,
                (
                    item["quantity"],
                    item["product_id"]
                )
            )


            response_items.append({
                "product_id": item["product_id"],
                "product_name": item["product_name"],
                "quantity": item["quantity"],
                "unit_price": float(item["unit_price"]),
                "item_price": float(item["item_price"])
            })


        # ----------------------------------------------------
        # STEP 5: Commit only after everything succeeds
        # ----------------------------------------------------

        connection.commit()


        # ----------------------------------------------------
        # STEP 6: Return response
        # ----------------------------------------------------

        return {
            "order_id": order_id,
            "user_id": order.user_id,
            "items": response_items,
            "order_total": float(order_total),
            "status": order_status,
            "created_at": created_at
        }


    except HTTPException:
        connection.rollback()
        raise

    except Exception as e:
        connection.rollback()

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

    finally:
        cursor.close()
        connection.close()


# ============================================================
# 6. GET ALL ORDERS FOR A USER
# ============================================================

@app.get("/users/{user_id}/orders")
def get_user_orders(user_id: int):

    connection = get_connection()
    cursor = connection.cursor()

    try:

        cursor.execute(
            """
            SELECT
                o.id AS order_id,
                u.name AS customer_name,
                o.status,
                o.total_amount,
                o.created_at
            FROM orders o
            JOIN users u
                ON o.user_id = u.id
            WHERE o.user_id = %s
            ORDER BY o.created_at DESC;
            """,
            (user_id,)
        )

        rows = cursor.fetchall()

        orders = []

        for row in rows:

            orders.append({
                "order_id": row[0],
                "customer_name": row[1],
                "status": row[2],
                "total_amount": float(row[3]),
                "created_at": row[4]
            })

        return orders

    finally:
        cursor.close()
        connection.close()


# ============================================================
# GET SINGLE ORDER
# ============================================================

@app.get("/orders/{order_id}")
def get_order(order_id: int):

    connection = get_connection()
    cursor = connection.cursor()

    try:

        # ----------------------------------------------------
        # Get order details
        # ----------------------------------------------------

        cursor.execute(
            """
            SELECT
                o.id,
                u.name,
                u.email,
                o.status,
                o.total_amount,
                o.created_at
            FROM orders o
            JOIN users u
                ON o.user_id = u.id
            WHERE o.id = %s;
            """,
            (order_id,)
        )

        order = cursor.fetchone()

        if order is None:
            raise HTTPException(
                status_code=404,
                detail="Order not found"
            )


        # ----------------------------------------------------
        # Get order items
        # ----------------------------------------------------

        cursor.execute(
            """
            SELECT
                p.name,
                oi.quantity,
                oi.unit_price,
                oi.item_price
            FROM order_items oi
            JOIN products p
                ON oi.product_id = p.id
            WHERE oi.order_id = %s
            ORDER BY oi.id;
            """,
            (order_id,)
        )

        item_rows = cursor.fetchall()

        items = []

        for row in item_rows:

            items.append({
                "product_name": row[0],
                "quantity": row[1],
                "unit_price": float(row[2]),
                "item_price": float(row[3])
            })


        return {
            "order_id": order[0],
            "customer_name": order[1],
            "customer_email": order[2],
            "status": order[3],
            "total_amount": float(order[4]),
            "created_at": order[5],
            "items": items
        }

    finally:
        cursor.close()
        connection.close()


# ============================================================
# PRODUCT SALES REPORT
# ============================================================

@app.get("/reports/product-sales")
def product_sales_report():

    connection = get_connection()
    cursor = connection.cursor()

    try:

        cursor.execute(
            """
            SELECT
                p.id,
                p.name,
                SUM(oi.quantity) AS total_quantity_sold,
                SUM(oi.item_price) AS total_revenue
            FROM products p
            JOIN order_items oi
                ON p.id = oi.product_id
            JOIN orders o
                ON oi.order_id = o.id
            WHERE o.status != 'cancelled'
            GROUP BY p.id, p.name
            ORDER BY total_revenue DESC;
            """
        )

        rows = cursor.fetchall()

        report = []

        for row in rows:

            report.append({
                "product_id": row[0],
                "product_name": row[1],
                "total_quantity_sold": float(row[2]),
                "total_revenue": float(row[3])
            })

        return report

    finally:
        cursor.close()
        connection.close()


# ============================================================
# CANCEL ORDER
# ============================================================

@app.patch("/orders/{order_id}/cancel")
def cancel_order(order_id: int):

    connection = get_connection()
    cursor = connection.cursor()

    try:

        # ----------------------------------------------------
        # STEP 1: Lock and check order
        # ----------------------------------------------------

        cursor.execute(
            """
            SELECT status
            FROM orders
            WHERE id = %s
            FOR UPDATE;
            """,
            (order_id,)
        )

        order = cursor.fetchone()

        if order is None:
            raise HTTPException(
                status_code=404,
                detail="Order not found"
            )

        current_status = order[0]

        if current_status == "cancelled":
            raise HTTPException(
                status_code=400,
                detail="Order is already cancelled"
            )


        # ----------------------------------------------------
        # STEP 2: Get order items
        # ----------------------------------------------------

        cursor.execute(
            """
            SELECT
                product_id,
                quantity
            FROM order_items
            WHERE order_id = %s;
            """,
            (order_id,)
        )

        items = cursor.fetchall()


        # ----------------------------------------------------
        # STEP 3: Restore inventory
        # ----------------------------------------------------

        for product_id, quantity in items:

            cursor.execute(
                """
                UPDATE products
                SET inventory = inventory + %s
                WHERE id = %s;
                """,
                (
                    quantity,
                    product_id
                )
            )


        # ----------------------------------------------------
        # STEP 4: Cancel order
        # ----------------------------------------------------

        cursor.execute(
            """
            UPDATE orders
            SET status = 'cancelled'
            WHERE id = %s;
            """,
            (order_id,)
        )


        connection.commit()

        return {
            "order_id": order_id,
            "status": "cancelled",
            "message": "Order cancelled and inventory restored"
        }


    except HTTPException:
        connection.rollback()
        raise

    except Exception as e:
        connection.rollback()

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

    finally:
        cursor.close()
        connection.close()

