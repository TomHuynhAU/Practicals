# shop_calculator.py

# Get the number of items from the user
while True:
    num_items = int(input("Number of items: "))
    if num_items >= 0:
        break
    else:
        print("Invalid number of items!")

# Initialize the total price
total_price = 0

# Calculate the total price of items
for i in range(num_items):
    price = float(input("Price of item: "))
    total_price += price

# Apply discount if total price is over $100
if total_price > 100:
    total_price *= 0.9  # 10% discount

# Display the total price
print(f"Total price for {num_items} items is ${total_price:.2f}")
