# temperatures.py

def celsius_to_fahrenheit(celsius):
    """Convert temperature from Celsius to Fahrenheit."""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    """Convert temperature from Fahrenheit to Celsius."""
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Get user input for temperature in Celsius
celsius_input = float(input("Enter temperature in Celsius: "))

# Convert Celsius to Fahrenheit and print the result
fahrenheit_result = celsius_to_fahrenheit(celsius_input)
print(f"{celsius_input} degrees Celsius is equal to {fahrenheit_result:.2f} degrees Fahrenheit.")

# Get user input for temperature in Fahrenheit
fahrenheit_input = float(input("Enter temperature in Fahrenheit: "))

# Convert Fahrenheit to Celsius and print the result
celsius_result = fahrenheit_to_celsius(fahrenheit_input)
print(f"{fahrenheit_input} degrees Fahrenheit is equal to {celsius_result:.2f} degrees Celsius.")
