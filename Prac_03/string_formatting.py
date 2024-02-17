# String formatting example
brand = "Gibson"
model = "L-5 CES"
year = 1922
cost = 16035

# Output using f-string formatting
print(f"{year} {brand} {model} for about ${cost:,}!")

# Output using for loop with range and string formatting
for i in range(0, 201, 50):
    print(f"{i:>3}")
