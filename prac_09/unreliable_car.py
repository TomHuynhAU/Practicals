import random
from car import Car

class UnreliableCar(Car):
    """Specialised version of a Car that includes reliability."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car a given distance based on its reliability."""
        random_number = random.uniform(0, 100)  # Generate a random number between 0 and 100
        if random_number < self.reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
        # print(f"Random number: {random_number}, Reliability: {self.reliability}, Distance driven: {distance_driven}")
        return distance_driven
