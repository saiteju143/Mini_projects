from logger import logging


class Restaurant:

    def __init__(self , name):
        self.name=name

class Customer:

    def __init__(self,customer_name):
        self.customer_name=customer_name

class Food_Items:

    def __init__(self,name,category,price):
            try:
                if price<=0:
                    raise ValueError("price cannot be zero")
                self.name=name
                self.category=category
                self.price=price
            except ValueError:
                print("price cannot be zero")
            logging.error("price cannot be zero")
          
            

class Orders:

    def __init__(self):
        self.orders=[]

    def check_availability(self,menu):
        try:
            select_dish=input("enter name of dish")
            for food_item in menu:
                if food_item.name==select_dish:
                    self.orders.append(food_item)
                    
                    logging.info(f"{food_item} appended successfully")
                    return True
            
            print(f"{select_dish} not available")
            logging.error(f"{food_item} not found successfully")
            return False
        except AttributeError as e:
            print(f"Invalid input:,{e}")
            return False

    def total_bill(self):
        try:
            total_bill=0
            for food_item in self.orders:
                if food_item.price<=0:
                    raise ValueError("price cannot be zero")
                total_bill+=food_item.price
                if food_item.price<=0:
                    raise ValueError("Price can never be zero")
            logging.info("Total Bill calculated")
            return total_bill
        except ValueError as e:
            print("Price can never be zero")
            return 0
        except Exception as e:
            print(f"Unexpected error while calculating total:,{e}")
            logging.error(f"Unexpected error while calculating total:,{e}")
            return 0
    
    def display(self):
        try:
            if not self.orders:
                print("No food items ordered")
                return
            for food_item in self.orders:
                print("|FOOD_ITEM :" , food_item.name,
                    "|CATEGORY :" , food_item.category,
                    "|PRICE :" , food_item.price)
        except AttributeError as e:
            print("Invalid input error:,{e}")
            return False
        except Exception as e:
            print(f"Unexpected error occured while displaying:,{e}")
            return False


restaurant=Restaurant("Mehfil")
customer1=Customer("Ravi")
customer2=Customer("Anil")
food_items1=Food_Items("Chicken_Biryani" , "Biryani",450)
food_items2=Food_Items("Paneer_Curry" , "Curries",350)
food_items3=Food_Items("Chicken_Tikka" , "Starters",369)
food_items4=Food_Items("Chicken_Manchow_Soup" , "Soups",160)
food_items5=Food_Items("Ice_Cream" , "Dessert",100)


print("    CUSTOMER1 ORDER DETAILS    ")
print(restaurant.name)
print(customer1.customer_name)

menu=[food_items1,food_items2,food_items3,food_items4,food_items5]

order=Orders()
number_of_items=int(input("enter number of items to select"))
for i in range(number_of_items):
    order.check_availability(menu)


print("\n Food_items ordered :")
order.display()
print("\n Total Price :" ,order.total_bill())


print("="*30)

print("    CUSTOMER2 ORDER DETAILS    ")
print(restaurant.name)
print(customer2.customer_name)

menu=[food_items1,food_items2,food_items3,food_items4,food_items5]

order=Orders()
number_of_items=int(input("enter number of items to select"))
for i in range(number_of_items):
    order.check_availability(menu)


print("\n Food_items ordered :")
order.display()
print("\n Total Price :" ,order.total_bill())
