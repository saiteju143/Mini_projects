from logger import logging

class vehicle:
    def __init__(self,vehicle_number,brand,driver_name,price_per_km):
        self.vehicle_number=vehicle_number
        self.brand=brand
        self.driver_name=driver_name
        self.price_per_km=price_per_km


class car(vehicle):

    def book_vehicle(self):
                try:
                    travel_distance=int(input("enter travel distance in km"))
                    if travel_distance<=0:
                           raise ValueError("Invalid input")
                    total_fare=self.price_per_km*travel_distance
                 
                    print("\n BOOKING DETAILS")
                    print("Driver:" , self.driver_name)
                    print("vehicle:" , self.brand)
                    print("Distance:" , travel_distance ,"KM") 
                    print("Rate:" , self.price_per_km ,"/km")
                    print("Total_fare:" , total_fare)
                    print("Cab booked successfully")
                    logging.info(f"Cab booked successfully- ,"
                                 f"Driver:{self.driver_name},"
                                 f"distance:{travel_distance},"
                                 f"Fare :{total_fare} ")
                except ValueError as e:
                       print(f"invalid input:{e}")
                       logging.error(f"Booking error:{e}")
                except Exception as e:
                       print(f"unexpected error:{e}")
                       logging.error(f"unexpected error:{e}")
                       



class bike(vehicle):

    def book_vehicle(self):
                try:
                    travel_distance=int(input("enter travel distance in km"))
                    if travel_distance<=0:
                        raise ValueError("Invalid input") 
                
                    total_fare=self.price_per_km*travel_distance
            
                    print("\n BOOKING DETAILS")
                    print("Driver:" , self.driver_name)
                    print("vehicle:" , self.brand)
                    print("Distance:" , travel_distance ,"KM") 
                    print("Rate:" , self.price_per_km ,"/km")
                    print("Total_fare:" , total_fare)
                    print("Bike booked successfully")
                    logging.info(f"Bike booked successfully- ,"
                                 f"Driver:{self.driver_name},"
                                 f"distance:{travel_distance},"
                                 f"Fare :{total_fare} ")
                except ValueError as e:
                        print(f"invalid input:{e}")
                        logging.error(f"Booking error:{e}")
                except Exception as e:
                        print(f"unexpected error:{e}")
                        logging.error(f"unexpected error:{e}")


car1=car("TS01AB1234", "Car", "Rahul", 20)
car2 = car("TS02CD5678", "Car", "Ramesh", 25)

bike1 = bike("TS03EF1234", "Bike", "Sai", 10)
bike2 = bike("TS04GH5678", "Bike", "Kiran", 15)

choice=input("enter vehicle (car1/car2/bike1/bike2)")

                
if choice=="car1":
       car1.book_vehicle()
elif choice=="car2":
       car2.book_vehicle()
elif choice=="bike1":
       bike1.book_vehicle()
elif choice=="bike2":
       bike2.book_vehicle()
else:
       print("invalid choice")


            


