# Base class: Device
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def turn_on(self):
        print(f"{self.brand} {self.model} is now ON!")

    def turn_off(self):
        print(f"{self.brand} {self.model} is now OFF!")

# Derived class: Smartphone (inherits from Device)
class Smartphone(Device):
    def __init__(self, brand, model, battery_life):
        super().__init__(brand, model)
        self.battery_life = battery_life

    def check_battery(self):
        print(f"Battery life: {self.battery_life} hours")

# Create an object of Smartphone
my_phone = Smartphone("Apple", "iPhone 13", 20)

# Using methods from both classes
my_phone.turn_on()
my_phone.check_battery()
my_phone.turn_off()
