class Wheel:
    def __init__(self, size: int):
        self.size = size

class Bicycle:
    def __init__(self, wheels: list[Wheel]):
        # The wheels are passed in from the outside.
        # If the Bicycle is destroyed, the wheels still exist.
        self.wheels = wheels

front_wheel = Wheel(26)
back_wheel = Wheel(26)

my_bike = Bicycle([front_wheel, back_wheel])
