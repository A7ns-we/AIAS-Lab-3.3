def get_customer_info():
    print("Enter Customer Information:")
    name = input("Name: ")
    customer_id = input("Customer ID: ")
    address = input("Address: ")
    return {
        "name": name,
        "customer_id": customer_id,
        "address": address
    }

def get_previous_bill():
    print("\nEnter Previous Bill Details:")
    prev_month = input("Previous Bill Month (e.g., May 2024): ")
    prev_amount = input("Previous Bill Amount: ")
    try:
        prev_amount = float(prev_amount)
    except ValueError:
        print("Invalid amount. Setting previous amount to 0.")
        prev_amount = 0.0
    return {
        "month": prev_month,
        "amount": prev_amount
    }

def calculate_power_bill(units):
    # Example slab rates:
    # 0-100 units: Rs. 5/unit
    # 101-200 units: Rs. 7/unit
    # 201+ units: Rs. 10/unit
    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = 100 * 5 + (units - 100) * 7
    else:
        bill = 100 * 5 + 100 * 7 + (units - 200) * 10
    return bill

def show_bill(customer, previous_bill, current_units, current_bill):
    print("\n--- Power Bill Details ---")
    print(f"Customer Name: {customer['name']}")
    print(f"Customer ID: {customer['customer_id']}")
    print(f"Address: {customer['address']}")
    print("\nPrevious Bill:")
    print(f"  Month: {previous_bill['month']}")
    print(f"  Amount: Rs. {previous_bill['amount']:.2f}")
    print("\nCurrent Bill:")
    print(f"  Units Consumed: {current_units}")
    print(f"  Amount: Rs. {current_bill:.2f}")

def main():
    customer = get_customer_info()
    previous_bill = get_previous_bill()
    print("\nEnter Current Month Details:")
    while True:
        units_input = input("Units Consumed: ")
        try:
            current_units = int(units_input)
            if current_units < 0:
                print("Units cannot be negative. Please enter again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer for units.")
    current_bill = calculate_power_bill(current_units)
    show_bill(customer, previous_bill, current_units, current_bill)

if __name__ == "__main__":
    main()
