"""
Emails Program
"""

def extract_name(email):
    # Split email address at '@' and take the first part
    name = email.split('@')[0]
    # Replace dots with spaces and title-case the name
    return name.replace('.', ' ').title()

def main():
    user_data = {}
    while True:
        email = input("Email: ")
        if email == "":
            break
        name = extract_name(email)
        is_correct = input(f"Is your name {name}? (Y/n) ").strip().lower()
        if is_correct in ['y', 'yes', '']:
            user_data[email] = name
        else:
            name = input("Name: ").strip().title()
            user_data[email] = name

    print("\nEmails and Names:")
    for email, name in user_data.items():
        print(f"{name} ({email})")

if __name__ == "__main__":
    main()
