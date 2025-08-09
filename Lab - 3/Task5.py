def convert_temperature():
    print("=== Temperature Conversion ===")
    print("Select conversion type:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        c = input("Enter temperature in Celsius: ")
        try:
            c = float(c)
            f = (c * 9/5) + 32
            print(f"{c}°C = {f:.2f}°F")
        except ValueError:
            print("Invalid input. Please enter a number.")
    elif choice == '2':
        f = input("Enter temperature in Fahrenheit: ")
        try:
            f = float(f)
            c = (f - 32) * 5/9
            print(f"{f}°F = {c:.2f}°C")
        except ValueError:
            print("Invalid input. Please enter a number.")
    elif choice == '3':
        c = input("Enter temperature in Celsius: ")
        try:
            c = float(c)
            k = c + 273.15
            print(f"{c}°C = {k:.2f}K")
        except ValueError:
            print("Invalid input. Please enter a number.")
    elif choice == '4':
        k = input("Enter temperature in Kelvin: ")
        try:
            k = float(k)
            c = k - 273.15
            print(f"{k}K = {c:.2f}°C")
        except ValueError:
            print("Invalid input. Please enter a number.")
    elif choice == '5':
        f = input("Enter temperature in Fahrenheit: ")
        try:
            f = float(f)
            k = (f - 32) * 5/9 + 273.15
            print(f"{f}°F = {k:.2f}K")
        except ValueError:
            print("Invalid input. Please enter a number.")
    elif choice == '6':
        k = input("Enter temperature in Kelvin: ")
        try:
            k = float(k)
            f = (k - 273.15) * 9/5 + 32
            print(f"{k}K = {f:.2f}°F")
        except ValueError:
            print("Invalid input. Please enter a number.")
    else:
        print("Invalid choice. Please select a valid option.")

def temperature_menu():
    while True:
        print("\n--- Temperature Conversion Menu ---")
        print("1. Convert Temperature")
        print("2. Exit")
        menu_choice = input("Enter your choice (1-2): ")
        if menu_choice == '1':
            convert_temperature()
        elif menu_choice == '2':
            print("Exiting Temperature Conversion Program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    temperature_menu()
