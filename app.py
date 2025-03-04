def display_banner():
    """Displays the application banner with a stylish intro."""
    print("\n🔥🔥 WELCOME TO THE DABANG UNIT CONVERTER 🔥🔥\n")
    print("🚀 Convert like a pro! Just pick a number and get results instantly! 💥\n")


def get_conversion_options():
    """Returns a list of available conversions with their symbols."""
    return [
        (1, 'km', 'mi', '🌍'),
        (2, 'mi', 'km', '🏁'),
        (3, 'kg', 'lbs', '🏋️'),
        (4, 'lbs', 'kg', '🦾'),
        (5, '°F', '°C', '🌡️'),
        (6, '°C', '°F', '🔥')
    ]


def display_conversion_options(conversions):
    """Displays available conversion options in a structured format."""
    print("🔹 Available Conversions:\n")
    for number, from_unit, to_unit, emoji in conversions:
        print(f"⚡ {number}) {from_unit} ➝ {to_unit} {emoji}")


def get_conversion_factors():
    """Returns a dictionary of conversion factors and formulas."""
    return {
        ('km', 'mi'): 0.621371,
        ('mi', 'km'): 1.60934,
        ('kg', 'lbs'): 2.20462,
        ('lbs', 'kg'): 0.453592,
        ('°F', '°C'): lambda f: (f - 32) * 5/9,
        ('°C', '°F'): lambda c: (c * 9/5) + 32
    }


def get_user_choice(conversions):
    """Handles user input for selecting a conversion type."""
    while True:
        try:
            choice = int(input("\n🎯 Enter the number of the conversion to use: "))
            if 1 <= choice <= len(conversions):
                return choice - 1
            else:
                print("❌ Invalid selection! Pick a number from the list.")
        except ValueError:
            print("⚠️ Please enter a valid numeric choice.")


def get_user_value(from_unit):
    """Handles user input for entering a value to convert."""
    while True:
        try:
            return float(input(f"\n💡 Enter value in {from_unit}: "))
        except ValueError:
            print("⚠️ Invalid input! Please enter a numeric value.")


def perform_conversion(from_unit, to_unit, from_value, conversion_factors):
    """Performs the actual unit conversion based on the factors provided."""
    conversion = conversion_factors.get((from_unit, to_unit))
    if callable(conversion):
        return conversion(from_value)
    return from_value * conversion


def main():
    """Main function to run the unit converter."""
    display_banner()
    conversions = get_conversion_options()
    display_conversion_options(conversions)
    
    # Get user selection
    choice_index = get_user_choice(conversions)
    _, from_unit, to_unit, emoji = conversions[choice_index]
    
    # Get value to convert
    from_value = get_user_value(from_unit)

    # Perform conversion
    conversion_factors = get_conversion_factors()
    result = perform_conversion(from_unit, to_unit, from_value, conversion_factors)

    # Display result
    print(f"\n✅ RESULT: {from_value} {from_unit} ➝ {result:.2f} {to_unit} {emoji}")


# Run the program
if __name__ == "__main__":
    main()
