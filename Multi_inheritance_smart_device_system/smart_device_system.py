
class Camera:
    def take_photo(self):
        print("Photo clicked successfully")
    def record_video(self):
        print("Video recorded successfully")

class Music_player:
    def play_music(self):
        print("Music is playing")
    def stop_music(self):
        print("Music stopped")

class GPS:
    def current_location(self):
        print("Current location accessed")
    def navigate(self):
        print("Navigation started")


class Smart_Phone(Camera,Music_player,GPS):
    def __init__(self,brand,model,price,storage):
        self.brand=brand
        self.model=model
        self.price=price
        self.storage=storage
    def display_details(self):
        print("Brand:" , self.brand)
        print("Model:" , self.model)
        print("Price:" , self.price)
        print("Storage:" , self.storage)


obj1=Smart_Phone("iphone" , "13pro" , 150000,"256GB")
obj2=Smart_Phone("Samsung" , "s25Ultra" , 140000,"256GB")
obj3=Smart_Phone("MI" , "12" , 50000,"128GB")


obj1.display_details()
obj2.display_details()
obj3.display_details()

obj1.current_location()
obj1.play_music()
obj1.navigate()