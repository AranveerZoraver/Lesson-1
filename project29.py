class Vehicle:
    def __init__(self, brand, wheels):
        self.brand = brand
        self.wheels = wheels

    def describe(self):
        return f"{self.brand} vehicle with {self.wheels} wheels"


class Car(Vehicle):
    def __init__(self, brand, wheels, doors):
        super().__init__(brand, wheels)
        self.doors = doors

    def describe(self):
        base = super().describe()
        return f"{base} and {self.doors} doors"


vehicle = Vehicle("Generic", 4)
car = Car("Toyota", 4, 4)

print(vehicle.describe())
print(car.describe())
print(issubclass(Car, Vehicle))
print(isinstance(car, Vehicle))