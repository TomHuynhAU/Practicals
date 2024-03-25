# myguitars.py
from guitar import Guitar

def load_guitars(filename):
    guitars = []
    with open(filename, 'r') as file:
        for line in file:
            data = line.strip().split(',')
            name, year, cost = data
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars

def display_guitars(guitars):
    print("All Guitars:")
    for guitar in guitars:
        print(guitar)

def add_new_guitar(guitars):
    name = input("Enter guitar name: ")
    year = int(input("Enter year made: "))
    cost = float(input("Enter cost: "))
    guitars.append(Guitar(name, year, cost))

def save_guitars(filename, guitars):
    with open(filename, 'w') as file:
        for guitar in guitars:
            file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")

def main():
    filename = "guitars.csv"
    guitars = load_guitars(filename)
    print("Loaded Guitars:")
    display_guitars(guitars)

    while True:
        print("\nMenu:")
        print("1. Add new guitar")
        print("2. Display all guitars")
        print("3. Quit")

        choice = input("Enter your choice: ")
        if choice == '1':
            add_new_guitar(guitars)
        elif choice == '2':
            display_guitars(guitars)
        elif choice == '3':
            save_guitars(filename, guitars)
            print("Guitars saved to file.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
