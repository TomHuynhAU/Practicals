import random

def determine_score_result(score):
    """Determine the result based on the score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def main():
    """Main function to execute the program."""
    user_score = float(input("Enter your score: "))
    user_result = determine_score_result(user_score)
    print("User's result:", user_result)

    # Generate a random score
    random_score = random.randint(0, 100)
    random_result = determine_score_result(random_score)
    print("Random score:", random_score)
    print("Random score result:", random_result)

if __name__ == "__main__":
    main()
