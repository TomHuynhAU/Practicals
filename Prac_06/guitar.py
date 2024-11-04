# Estimated time: 15 minutes

from datetime import date

# Start time: 10:25 AM

class Guitar:
    """Represents a guitar with various attributes."""

    def __init__(self, name="", year=0, cost=0):
        """Initialize a Guitar instance with specified attributes."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of the Guitar instance."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Return the age of the guitar in years."""
        current_year = date.today().year
        return current_year - self.year

    def is_vintage(self):
        """Check if the guitar is vintage."""
        return self.get_age() >= 50

# End time: 10:40 AM
