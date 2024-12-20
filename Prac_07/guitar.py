# guitar.py tomhuynh
class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.year} {self.name} : ${self.cost:.2f}"

    def get_age(self):
        return 2024 - self.year

    def is_vintage(self):
        return self.get_age() >= 50
