# Estimated time: 10 minutes

from guitar import Guitar

# Start time: 10:45 AM

def main():
    """Test program for Guitar class."""
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2013)

    print(f"{gibson.name} get_age() - Expected 100. Got {gibson.get_age()}")
    print(f"{another_guitar.name} get_age() - Expected 9. Got {another_guitar.get_age()}")

    print(f"{gibson.name} is_vintage() - Expected True. Got {gibson.is_vintage()}")
    print(f"{another_guitar.name} is_vintage() - Expected False. Got {another_guitar.is_vintage()}")

if __name__ == "__main__":
    main()

# End time: 10:55 AM
