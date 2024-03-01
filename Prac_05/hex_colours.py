"""
Intermediate Exercise: Hexadecimal Color Codes Lookup
"""

# Dictionary of color names and their corresponding hexadecimal codes
COLOR_CODES = {
    "ALICEBLUE": "#F0F8FF",
    "ANTIQUEWHITE": "#FAEBD7",
    "AQUA": "#00FFFF",
    "AZURE": "#F0FFFF",
    "BEIGE": "#F5F5DC",
    "BISQUE": "#FFE4C4",
    "BLACK": "#000000",
    "BLANCHEDALMOND": "#FFEBCD",
    "BLUE": "#0000FF",
    "BLUEVIOLET": "#8A2BE2"
}


def get_hex_color(color_name):
    """Look up hexadecimal color code."""
    return COLOR_CODES.get(color_name.upper(), "Invalid color name")


def main():
    print("Welcome to Hexadecimal Color Codes Lookup")
    print("Available color names:")
    print(", ".join(COLOR_CODES.keys()))

    while True:
        color_name = input("Enter color name (or blank to quit): ").upper()
        if not color_name:
            break
        hex_code = get_hex_color(color_name)
        print(f"The hexadecimal code for {color_name} is {hex_code}")


if __name__ == "__main__":
    main()
