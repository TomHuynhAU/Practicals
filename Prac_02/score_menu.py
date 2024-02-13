import random
from score import determine_score_result

def get_valid_score():
    """Get a valid score from the user (0-100 inclusive)."""
    while True:
        score = float(input("Enter a score (0-100 inclusive): "))
        if 0 <= score <= 100:
            return score
        else:
            print("Invalid score. Please enter a score between 0 and 100.")

def print_result(score):
    """Print the result for the given score."""
    result = determine_score_result(score)
    print("Result:", result)

def show_stars(score):
    """Print stars based on the score."""
    print("*" * int(score))

def main():
    """Main function to execute the program."""
    print("Welcome to Score Menu!")
    user_score = get_valid_score()

    while True:
        print("\nMenu:")
        print("(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")

        choice = input(">>> ").upper()

        if choice == 'G':
            user_score = get_valid_score()
        elif choice == 'P':
            print_result(user_score)
        elif choice == 'S':
            show_stars(user_score)
        elif choice == 'Q':
            print("Thank you for using Score Menu. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter G, P, S, or Q.")

if __name__ == "__main__":
    main()
