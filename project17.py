def calculate_change(due_amount, amount_paid):
    """Returns the change owed once the due amount is paid."""
    return amount_paid - due_amount


valid_coins = [1, 5, 10, 25]
due_amount = 60
amount_paid = 0

while True:
    coin = int(input("Insert a coin (1, 5, 10, 25): "))
    if coin not in valid_coins:
        print("Invalid coin, try again.")
        continue
    amount_paid += coin
    if amount_paid >= due_amount:
        break

change = calculate_change(due_amount, amount_paid)
if change == 0:
    pass
else:
    print(f"Change due: {change}")

print(f"Parking fee: {due_amount} | Paid: {amount_paid} | Change: {change}")