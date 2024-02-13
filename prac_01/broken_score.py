#broken_score

# Input score from the user
score = float(input("Enter score: "))

# Check if the score is invalid
if score < 0 or score > 100:
    print("Invalid score")
# Check if the score is excellent
elif score >= 90:
    print("Excellent")
# Check if the score is passable
elif score >= 50:
    print("Passable")
# If the score is not excellent or passable, it is bad
else:
    print("Bad")
