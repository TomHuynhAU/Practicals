# Question 1: Write user's name to a file
name = input("Enter your name: ")
with open("name.txt", "w") as file:
    file.write(name)

# Question 2: Read name from file and print it
with open("name.txt", "r") as file:
    name = file.read().strip()
    print(f"Your name is {name}")

# Question 3: Read first two numbers from "numbers.txt" and print their sum
with open("numbers.txt", "r") as file:
    first_number = int(file.readline().strip())
    second_number = int(file.readline().strip())
    total = first_number + second_number
    print(f"The sum of the first two numbers is: {total}")

# Question 4: Read all numbers from "numbers.txt" and print their total
with open("numbers.txt", "r") as file:
    total = sum(int(line.strip()) for line in file)
    print(f"The total sum of all numbers is: {total}")
