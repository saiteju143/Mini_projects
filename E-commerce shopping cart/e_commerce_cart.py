import logging
logging.basicConfig(filename="ecommerce.log" , level=logging.INFO,format="%(asctime)s-%(levelname)s-%(message)s")


class product:

    def __init__(self,product_id,product_name,category,price,available_stock):
        try:

            self.product_id=product_id
            self.product_name=product_name
            self.category=category
            self.price=price
            self.available_stock=available_stock
            logging.info(f"Prodcut added successfully:{product_name}")
        except Exception as e:
            logging.error(f"unexpected error:{e}")


class shopping_cart:

    def __init__(self):
        self.cart_items=[]
        logging.info("shopping cart created")

    def check_availability(self,product):
        try:
            if product.available_stock > 0:
                logging.info(f"{product.product_name} is available in stock")
                return True
            else:
                logging.info(f"{product.product_name} is available in stock")
                return False
        except AttributeError as e:
            print("Invalid product: {e}")
            logging.error("Invalid product entered")
            return False
    def add_product(self,product):
        try:
            if self.check_availability(product):
                self.cart_items.append(product)
                product.available_stock-=1
                logging.info(f"{product.product_name} added to cart successfully")
                print(f"{product.product_name} added to cart successfully")
            else:
                logging.error(f"{product.product_name} not found or out of stock")
                print(f"{product.product_name} not available")
        except AttributeError as e:
            print(f"Invalid product:{e}")
            logging.error("Invalid product:{e}")
        except Exception as e:
            print(f"unexpected error while adding product to cart:{e}")
            logging.error(f"unexpected error while adding product to cart:{e}")

    def remove_product(self,product):
        try:
            if product in self.cart_items:
                self.cart_items.remove(product)
                product.available_stock+=1
                logging.info(f"{product.product_name} removed to cart successfully")
                print(f"{product.product_name} removed from cart successfully")
            else:
                logging.error(f"{product.product_name} not available in cart")
                print(f"{product.product_name} not available")
        except AttributeError as e:
            print(f"Invalid product:{e}")
            logging.error(f"Invalid product:{e}")
        except Exception as e:
            print(f"unexpected error while removing product from cart:{e}")
            logging.error(f"unexpected error while removing product from cart:{e}")

    def display_products(self):
        try:
            if not self.cart_items:
                print("Cart is empty")
                logging.info("cart is empty")
            else:
                for product in self.cart_items:
                    print("\n PRODUCTS IN SHOPPING CART")
                    print("ID :",product.product_id,
                          "| NAME :",product.product_name,
                          "| CATEGORY :",product.category,
                          "| PRICE :",product.price)

                logging.info("Products displayed successfully")
        except Exception as e:
            print(f"error while displaying products:{e}")
            logging.error(f"error while displaying products:{e}")


    def calculate_total(self):
        try:
            if not self.cart_items:
                print("Cart is empty")
                logging.info("cart is empty")
            else:
                total=0
                for product in self.cart_items:
                    total+=product.price
                logging.info(f"Total amount of products :{total}")
                return total
        except TypeError as e:
            print(f"invalid input:{e}")
            logging.error(f"invalid price found:{e}")
            return 0
        except Exception as e:
            print(f"invalid type of data entered:{e}")
            return 0


product1 = product(
    1,
    "Laptop",
    "Electronics",
    50000,
    5
)

product2 = product(
    2,
    "Mobile",
    "Electronics",
    25000,
    3
)

product3 = product(
    3,
    "Shoes",
    "Fashion",
    2000,
    10
)

product4 = product(
    4,
    "Watch",
    "Accessories",
    5000,
    2
)

# Product with zero stock

product5 = product(
    5,
    "Headphones",
    "Electronics",
    3000,
    0
)

cart=shopping_cart()
cart.add_product(product1)
cart.add_product(product2)
cart.add_product(product3)
cart.add_product(product4)
cart.add_product(product5)

cart.display_products()
print("\n Total amount:",cart.calculate_total())
cart.remove_product(product3)

print("\n After removing product")

cart.display_products()

print("\n Total amount:",cart.calculate_total())












