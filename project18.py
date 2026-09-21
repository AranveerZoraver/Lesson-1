def get_discount_rate(bill_amount):
    if bill_amount >= 5000:
        return 0.20
    elif bill_amount >= 2000:
        return 0.10
    elif bill_amount >= 500:
        return 0.05
    return 0.0


while True:
    try:
        bill_amount = float(input("Enter your total shopping bill amount: $"))
        num_items = int(input("Enter the number of items purchased: "))

        if bill_amount < 0:
            raise ValueError("Bill amount cannot be negative")
        if num_items < 0:
            raise ValueError("Number of items cannot be negative")

        discount_rate = get_discount_rate(bill_amount)
        discount_amount = bill_amount * discount_rate
        final_amount = bill_amount - discount_amount
        price_per_item = final_amount / num_items

    except ValueError as e:
        print(f"Invalid input: {e}. Please enter valid numbers.\n")
        continue
    except ZeroDivisionError:
        print("Number of items cannot be zero. Please try again.\n")
        continue
    else:
        print("\n--- Shopping Bill Summary ---")
        print(f"Original Bill:      ${bill_amount:.2f}")
        print(f"Discount Rate:      {discount_rate * 100:.0f}%")
        print(f"Discount Amount:    ${discount_amount:.2f}")
        print(f"Final Amount:       ${final_amount:.2f}")
        print(f"Price per Item:     ${price_per_item:.2f}")
        break
    finally:
        print("Attempt processed.\n")