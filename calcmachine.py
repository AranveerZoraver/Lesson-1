def calculate_price (paid,price):
    change = paid - price
    return change

snack_price = 25

print("====VENDING MACHINE====")
print("this snack costs {snack_price} units")
print("accepted coins: 1, 5, 10, 25,\n")


total_inserted = 0
coins_inserted = 0

while true:
    coin = int(input("insert a coin (1, 5, 10, or 25): "))

    if coin != 1 and coin   