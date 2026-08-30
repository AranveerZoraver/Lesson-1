print("=== Grocery Billing Queue ===\n")

all_items = []
customer_num = 1

while True:
    customer_name = input(f"Customer #{customer_num} name (or 'done' to finish billing): ").strip()
    if customer_name.lower() == "done":
        break

    print(f"\nBilling items for {customer_name}:")
    customer_total = 0.0

    while True:
        item_name = input("  Item name (or 'done' to finish this customer): ").strip()
        if item_name.lower() == "done":
            break

        category = input("  Category (Produce/Dairy/Bakery/Pantry/Other): ").strip().title() or "Other"
        price_text = input("  Price: $").strip()

        try:
            price = float(price_text)
        except ValueError:
            print("  Please enter a valid number for price.\n")
            continue

        if price <= 0:
            print("  Price must be greater than 0.\n")
            continue

        all_items.append({"customer": customer_name, "name": item_name, "category": category, "price": price})
        customer_total += price
        print(f"  Added {item_name} - ${price:.2f}\n")

    print(f"{customer_name}'s total: ${customer_total:.2f}\n")
    customer_num += 1

categories = {}
for item in all_items:
    categories.setdefault(item["category"], []).append(item)

print("=== Price-Category Report ===")
for category, items in categories.items():
    print(f"\n{category}")
    category_total = 0.0
    for item in items:
        print(f"  {item['name']} ({item['customer']}) - ${item['price']:.2f}")
        category_total += item["price"]
    print(f"  Subtotal: ${category_total:.2f}")