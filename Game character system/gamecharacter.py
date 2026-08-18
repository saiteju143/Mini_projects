from logger import logging

class game_character:
    def __init__(self,name,health,level):
        try:
            if health<=0:
                raise ValueError("Health cannot be zero")
            if level<=0:
                raise ValueError("level cannot be zero")
            self.name=name
            self.health=health
            self.level=level
        except ValueError as e:
            print(f"Invalid imput: {e}")
            logging.error(f"Invalid imput: {e}")
class Warrior(game_character):
    def __init__(self,name,health,level,weapon,strength):
        super().__init__(name,health,level)
        self.weapon=weapon
        self.strength=strength

    def attack(self,opponent):
        try:
            if self.strength<=0:
                raise ValueError("Strength cannot be zero")
            opponent.health-=self.strength
            if opponent.health<0:
                opponent.health=0
            print(f"{self.name} attacks {opponent.name}")
            print(f"{opponent.name}health is now {opponent.health}")
            logging.info(f"{self.name} attacks {opponent.name},"
                         f"using:{self.weapon},"
                         f"Damage:{self.strength},"
                         f"{opponent.name}health is now {opponent.health}")
        except AttributeError as e:
            print(f"invalid opponent:{e}")
            logging.error(f"invalid attack:{e}")
        except ValueError as e:
            print(f"Invalid input:{e}")
            logging.error(f"Invalid input:{e}")
        except Exception as e:
            print(f"Unexpected error:{e}")
            logging.error(f"unexpected error:{e}")




class Archer(game_character):

    def __init__(self, name, health, level,bow,arrows):
        super().__init__(name, health, level)
        self.bow=bow
        self.arrows=arrows

    def attack(self,opponent):
        try:
            if self.arrows<=0:
                raise ValueError("No arrows available")
            damage=15
            opponent.health-=damage
            self.arrows-=1
            if opponent.health<0:
                opponent.health=0
            print(f"{self.name} attacks {opponent.name}")
            print(f"{opponent.name}health is now {opponent.health}")
            logging.info(f"{self.name} attacks {opponent.name},"
                         f"using:{self.bow},"
                         f"Damage:{damage}"
                         f"{opponent.name} health is now {opponent.health}")
        except AttributeError as e:
                print(f"invalid opponent:{e}")
                logging.error(f"invalid attack:{e}")
        except ValueError as e:
            print(f"Invalid input:{e}")
            logging.error(f"Invalid input:{e}")
        except Exception as e:
            print(f"Unexpected error:{e}")
            logging.error(f"unexpected error:{e}")

class Wizard(game_character):

    def __init__(self, name, health, level,magic_power,spell):
        super().__init__(name, health, level)
        self.magic_power=magic_power
        self.spell=spell
    def attack(self,opponent):
        try:
            if self.magic_power<=0:
                raise ValueError("Magic power should be more than zero")
            
            opponent.health-=self.magic_power
            if opponent.health<0:
                opponent.health=0

            print(f"{self.name} attacks {opponent.name}")
            print(f"{opponent.name}health is now {opponent.health}")
            logging.info(
                    f"{self.name} attacked {opponent.name} "
                    f"using {self.spell}. "
                    f"Damage: {self.magic_power}, "
                    f"Remaining health: {opponent.health}")
        except AttributeError as e:
                print(f"invalid opponent:{e}")
                logging.error(f"invalid attack:{e}")
        except ValueError as e:
            print(f"Invalid input:{e}")
            logging.error(f"Invalid input:{e}")
        except Exception as e:
            print(f"Unexpected error:{e}")
            logging.error(f"unexpected error:{e}")
        
        



warrior1=Warrior("Arjun", 100, 5, "Sword", 20)
archer1=Archer("Rahul", 100, 4, "gold_bow", 5)
wizard1=Wizard("Kishore", 100, 8, 25, "fire_ball")

warrior1.attack(archer1)
warrior1.attack(wizard1)
archer1.attack(warrior1)
archer1.attack(wizard1)
wizard1.attack(warrior1)
wizard1.attack(archer1)
