class Engine:
    def __init__(self, horsepower: int):
        self.horsepower = horsepower

class Car:
    def __init__(self, horsepower: int):
        # The Engine is created INSIDE the Car constructor.
        # It lives and dies exclusively with the Car instance.
        self.engine = Engine(horsepower)

my_car = Car(300)
  
