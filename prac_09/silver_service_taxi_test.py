from silver_service_taxi import SilverServiceTaxi

def main():
    # Create a new SilverServiceTaxi object
    fancy_taxi = SilverServiceTaxi("Hummer", 200, 2)  # fanciness of 2

    # Print the details of the taxi
    print(fancy_taxi)

    # Drive the taxi 18 km
    fancy_taxi.drive(18)
    # Print the details and the current fare
    print(fancy_taxi)
    print(f"Current fare: ${fancy_taxi.get_fare():.2f}")

    # Use assert to test the fare calculation
    assert fancy_taxi.get_fare() == 48.78, f"Expected fare was 48.78 but got {fancy_taxi.get_fare():.2f}"

if __name__ == '__main__':
    main()
