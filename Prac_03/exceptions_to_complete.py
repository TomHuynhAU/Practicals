is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        # TODO: Add a line to set is_finished to True to exit the loop if a valid integer is entered
        is_finished = True
    except ValueError:  # TODO: Specify the exception you want to catch after except
        print("Please enter a valid integer.")

print("Valid result is:", result)
