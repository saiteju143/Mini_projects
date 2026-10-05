from fastapi import FastAPI,HTTPException,status
from database import get_connection
from pydantic import BaseModel,Field
from typing import Optional,Literal


app =FastAPI(
    title="Mini E-commerce API",
    description="FASTapi +Postresql E-commerce Backend",
    version="1.0.0"
)


class CreateUser(BaseModel):
    name:str=Field(...,min_length=3)
    email:str=Field(...,min_length=3)
class ProductCreate(BaseModel):
    name:str=Field(...,min_length=3)
    description:str|None=None
    price:float=Field(...,gt=0)
    inventory:int=Field(...,ge=0)
class Updateinventory(BaseModel):
    inventory:int=Field(...,ge=0)
class OrderItemCreate(BaseModel):
    product_id:int=Field(...,gt=0)
    quantity:int=Field(...,gt=0)
class OrderCreate(BaseModel):
    user_id:int=Field(...,gt=0)
    items:list[OrderItemCreate]

@app.post("/user_account")
def create_user(user:CreateUser):
    connection=get_connection()
    cursor=connection.cursor()
    try:

        cursor.execute("""
        INSERT INTO users 
        (name,email)
        VALUES (%s,%s)
        RETURNING id,name,email,created_at;
        """,(user.name,user.email))
        new_user=cursor.fetchone()
        connection.commit()
        return{
            "id": new_user[0],
            "name": new_user[1],
            "email": new_user[2],
            "created_at": new_user[3]
        }
    except Exception as e:
        connection.rollback()
        return {
            "error":str(e)
        }
    finally:
        cursor.close()
        connection.close()

@app.post("/products",status_code=201)
def view_products(product:ProductCreate):
    connection=get_connection()
    cursor=connection.cursor()
    try:
        cursor.execute("""
        INSERT INTO products
        (name,description,price,inventory)
        VALUES (%s,%s,%s,%s)
        RETURNING id,name,description,price,inventory,created_at;
        """,(product.name,product.description,product.price,product.inventory))
        new_product=cursor.fetchone()
        connection.commit()
        return{
            "id": new_product[0],
            "name": new_product[1],
            "description": new_product[2],
            "price": float(new_product[3]),
            "inventory": new_product[4],
            "created_at": new_product[5]
        }
    except Exception as e:
        connection.rollback()
        return{
            "error":str(e)
        }
    finally:
        cursor.close()
        connection.close()

@app.get("/view_products")
def get_prodcuts():
    connection=get_connection()
    cursor=connection.cursor()
    
    cursor.execute("""
    SELECT * FROM products
    ORDER BY id
    """)
    rows=cursor.fetchall()
    cursor.close()
    connection.close()
    products=[]
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

@app.put("/products/{product_id}/inventory")
def update_inventory(product_id:int,inventory_data:Updateinventory):
    connection=get_connection()
    cursor=connection.cursor()
    
    cursor.execute("""
    UPDATE products
    SET inventory=%s
    WHERE id=%s
    RETURNING id,name,inventory;
    """,(inventory_data.inventory,product_id))
    updated_product=cursor.fetchone()
    if updated_product is None:
        connection.rollback()
        cursor.close()
        connection.close()
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )
    connection.commit()
    cursor.close()
    connection.close()
    return{
    "id": updated_product[0],
    "name": updated_product[1],
    "inventory": updated_product[2]
}

@app.post("/orders",status_code=201)
def create_order(order:OrderCreate):
    connection=get_connection
    cursor=connection.cursor()
    try:
        cursor.execute("""
        SELECT id FROM 
        users
        WHERE id=%s;
        """,(order.user_id,))
        user=cursor.fetchone()
        if user is None:
            raise HTTPException(
                status_code=404,
                detail="User_id not found"
            )

        cursor.execute("""
        INSERT INTO orders
        (user_id,total_amount)
        VALUES (%s,%s)
        RETURNING id;
            """,(order.user_id,0))
        order_id=cursor.fetchone()[0]
        order_total=0
        order_item_response=[]
        for item in order.items:
            cursor.execute("""
            SELECT 
                id,name,price,inventory
            FROM products
            WHERE id=%s
            FOR UPDATE;
            """,(item.product_id,))
            product=cursor.fetchone()
            if not product:
                raise HTTPException(
                    status_code=404,
                    detail=f"product {item.product_id} not found"
                )
            product_id=product[0]
            product_name=product[1]
            unit_price=product[2]
            inventory=product[3]
            if inventory<item.quantity:
                raise HTTPException(
                    status_code=400,
                    detail=f"Not enough inventory {product_name}"
                )
            item_total=(item.quantity*unit_price)
            cursor.execute("""
            INSERT INTO order_items
            (order_id,product_id,unit_price,quantity,item_total)
            VALUES(%s,%s,%s,%s,%s)
                """,order_id,product_id,unit_price,item.quantity,item_total)
            cursor.execute("""
            UPDATE products
            SET inventory = inventory - %s
            WHERE id=%s;
                """,item.quantity,product_id)
            order_total+=item_total
            order_item_response.append({
                "product_id": product_id,
                "product_name": product_name,
                "quantity": item.quantity,
                "unit_price": float(unit_price),
                "item_total": float(item_total)
            })
            cursor.execute("""
            UPDATE orders
            SET total_amount=%s
            WHERE id=%s;
                """,order_total,order_id)
            connection.commit()
            return {
            "order_id": order_id,
            "user_id": order.user_id,
            "items": order_item_response,
            "order_total": float(order_total),
            "status": "placed"
        }
    except HTTPException:
        connection.rollback()
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
    finally:
        cursor.close()
        connection.close()

@app.get("/users/{user_id}/orders")
def get_user_orders(user_id:int):
    connection=get_connection()
    cursor=connection.cursor()
    cursor.execute("""
    SELECT 
    o.id AS order_id,
    u.name AS customer_name,
    o.status,
    o.total_amount,
    o.created_at
    FROM orders O
    JOIN USERS u
    ON o.user_id=u.id
    WHERE id=%s;
    ORDER BY o.created_at DESC;
""",(user_id,))
    rows=cursor.fetchall()
    cursor.close()
    connection.close()
    orders=[]
    for row in rows:
        orders.append({
            "order_id": row[0],
            "customer_name": row[1],
            "status": row[2],
            "total_amount": float(row[3]),
            "created_at": row[4]
        })
    return orders

@app.get("/orders/{order_id}")
def ger_order(order_id:int):
    connection=get_connection
    cursor=connection.cursor()
    cursor.execute("""
    SELECT 
        o.id,
        u.name,
        u.email,
        o.status,
        o.total_amount,
        o.created_at
        FROM orders o
        JOIN users u
        ON o.user_id=u.id
        WHERE o.id=%s;
""",(order_id,))
    order = cursor.fetchone()

    if order is None:

        cursor.close()

        connection.close()

        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )
    cursor.execute(
        """
        SELECT
            p.name,
            oi.quantity,
            oi.unit_price,
            oi.item_total

        FROM order_items oi

        JOIN products p
            ON oi.product_id = p.id

        WHERE oi.order_id = %s

        ORDER BY oi.id;
        """,
        (order_id,)
    )

    items = cursor.fetchall()
    cursor.close()
    connection.close()
    return {
        "order_id": order[0],

        "customer_name": order[1],

        "customer_email": order[2],

        "status": order[3],

        "order_total": float(order[4]),

        "created_at": order[5],

        "items": [
            {
                "product_name": item[0],
                "quantity": item[1],
                "unit_price": float(item[2]),
                "item_total": float(item[3])
            }

            for item in items
        ]
    }
@app.get("/reports/product-sales")
def product_sales_report():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT

            p.id,

            p.name,

            SUM(oi.quantity) AS total_quantity_sold,

            SUM(oi.item_total) AS total_revenue

        FROM products p

        JOIN order_items oi
            ON p.id = oi.product_id

        JOIN orders o
            ON oi.order_id = o.id

        WHERE o.status != 'cancelled'

        GROUP BY
            p.id,
            p.name

        ORDER BY total_revenue DESC;
        """
    )

    rows = cursor.fetchall()

    cursor.close()

    connection.close()


    return [
        {
            "product_id": row[0],
            "product_name": row[1],
            "total_quantity_sold": row[2],
            "total_revenue": float(row[3])
        }

        for row in rows
    ]

@app.patch("/orders/{order_id}/cancel")
def cancel_order(order_id: int):

    connection = get_connection()

    cursor = connection.cursor()

    try:

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


        if order[0] == "cancelled":

            raise HTTPException(
                status_code=400,
                detail="Order already cancelled"
            )


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

        for product_id, quantity in items:

            cursor.execute(
                """
                UPDATE products

                SET inventory =
                    inventory + %s

                WHERE id = %s;
                """,
                (
                    quantity,
                    product_id
                )
            )

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
            "message": "Order cancelled successfully",
            "order_id": order_id,
            "status": "cancelled"
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



