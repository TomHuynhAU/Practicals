# menus.py

# Get the name from the user
name = input("Enter name: ")

# Display the menu
print("(H)ello")
print("(G)oodbye")
print("(Q)uit")

# Get the initial choice from the user
choice = input(">>> ").upper()

# Menu-driven loop
while choice != 'Q':
    if choice == 'H':
        print(f"Hello {name}")
    elif choice == 'G':
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")

    # Display the menu again
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")

    # Get the next choice from the user
    choice = input(">>> ").upper()

# Display finished message
print("Finished.")
