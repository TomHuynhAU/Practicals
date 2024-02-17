import random

# Constants
MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 1.0
MAX_PRICE = 100.0
INITIAL_PRICE = 10.0
OUTPUT_FILE = "stock_prices.txt"

# Open file for writing
out_file = open(OUTPUT_FILE, 'w')

price = INITIAL_PRICE
print(f"Starting price: ${price:,.2f}", file=out_file)

# Simulate stock price for a number of days
for day in range(1, 426):
    # Calculate price change
    price_change = 0
    if random.randint(1, 2) == 1:
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        price_change = random.uniform(-MAX_DECREASE, 0)

    # Update price
    price *= (1 + price_change)
    price = max(MIN_PRICE, min(price, MAX_PRICE))  # Ensure price stays within allowed range

    # Output price to file
    print(f"On day {day} price is: ${price:.2f}", file=out_file)

# Close the file
out_file.close()
