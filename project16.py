def calculate_bill(price, quantity, tax_percent):
    subtotal = price * quantity
    total = subtotal + (subtotal * tax_percent / 100)
    return round(total, 2)


def tables_needed(num_guests, seats_per_table):
    """Recursively works out how many tables are needed to seat everyone."""
    if num_guests <= seats_per_table:
        return 1
    return 1 + tables_needed(num_guests - seats_per_table, seats_per_table)


bill = calculate_bill(12.50, 4, 5)
print(f"Total bill: {bill}")

tables = tables_needed(23, 4)
print(f"Tables needed: {tables}")

print(tables_needed.__doc__)