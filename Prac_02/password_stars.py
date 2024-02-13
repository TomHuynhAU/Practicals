# password_stars.py

def get_password():
    """Get a password from the user and return it."""
    password = input("Enter your password: ")
    return password

def print_asterisks(password):
    """Print asterisks based on the length of the password."""
    print("*" * len(password))

def main():
    """Main function to execute the program."""
    password = get_password()
    print_asterisks(password)

if __name__ == "__main__":
    main()
