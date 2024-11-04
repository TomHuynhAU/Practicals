# Estimated time: 20 minutes

from datetime import datetime

# Start time: 10:00 AM

class ProgrammingLanguage:
    """Represents a programming language with various attributes."""

    def __init__(self, name, typing, reflection, year):
        """Initialize a ProgrammingLanguage instance with specified attributes."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Check if the programming language is dynamically typed."""
        return self.typing == "Dynamic"

    def __str__(self):
        """Return a string representation of the ProgrammingLanguage instance."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

# End time: 10:20 AM
