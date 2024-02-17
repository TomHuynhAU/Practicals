try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator (not equal to zero): "))

    if denominator == 0:
        print("Denominator cannot be zero!")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")

print("Finished.")
