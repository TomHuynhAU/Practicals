from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

def display_menu():
    print("q)uit, c)hoose taxi, d)rive")

def display_taxis(taxis):
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    bill_to_date = 0.0

    print("Let's drive!")
    display_menu()
    choice = input(">>> ").lower()

    while choice != "q":
        if choice == "c":
            display_taxis(taxis)
            taxi_choice = input("Choose taxi: ")
            try:
                taxi_choice = int(taxi_choice)
                if 0 <= taxi_choice < len(taxis):
                    current_taxi = taxis[taxi_choice]
                else:
                    print("Invalid taxi choice")
            except ValueError:
                print("Invalid input; enter a valid number")
        elif choice == "d":
            if current_taxi:
                distance = input("Drive how far? ")
                try:
                    distance = int(distance)
                    current_taxi.start_fare()
                    distance_driven = current_taxi.drive(distance)
                    trip_cost = current_taxi.get_fare()
                    print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
                    bill_to_date += trip_cost
                except ValueError:
                    print("Invalid input; enter a valid number")
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")

        print(f"Bill to date: ${bill_to_date:.2f}")
        display_menu()
        choice = input(">>> ").lower()

    print(f"Total trip cost: ${bill_to_date:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)

if __name__ == "__main__":
    main()
