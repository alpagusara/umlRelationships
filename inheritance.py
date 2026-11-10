class Animal:
    def __init__(self, name: str):
        self.name = name

    def breathe(self):
        print(f"{self.name} is breathing.")

# Dog inherits from Animal
class Dog(Animal):
    def bark(self):
        print(f"{self.name} says Woof!")

dog = Dog("Buddy")
dog.breathe()  # Inherited method
dog.bark()     # Class-specific method
