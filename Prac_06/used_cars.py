"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from prac_06.car import Car

def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180, "My Car")
    my_car.drive(30)
    print(f"Car has fuel: {my_car.fuel}")
    print(my_car)

    limo = Car(100, "Limo")  # 1. Create a new Car object called "limo" that is initialised with 100 units of fuel.
    limo.add_fuel(20)  # 2. Add 20 more units of fuel to this new car object using the add method.
    print(f"Amount of fuel in the car: {limo.fuel}")  # 3. Print the amount of fuel in the car.
    limo.drive(115)  # 4. Attempt to drive the car 115 km using the drive method.
    print(limo)  # 5. Print the car object using the __str__ method

main()
