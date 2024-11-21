from unreliable_car import UnreliableCar

def main():
    # Create a new UnreliableCar object
    unreliable_car = UnreliableCar("Dodgy", 100, 50)  # 50% reliability
    reliable_car = UnreliableCar("Sultan", 100, 5)   #5% reliability

    # Attempt to drive the car 40 km
    distance_driven = reliable_car.drive(40)
    print(f"Attempted to drive 40 km. Actually drove: {distance_driven} km")
    print(reliable_car)

    # Attempt to drive the car another 60 km
    distance_driven = unreliable_car.drive(60)
    print(f"Attempted to drive 60 km. Actually drove: {distance_driven} km")
    print(unreliable_car)

if __name__ == '__main__':
    main()
