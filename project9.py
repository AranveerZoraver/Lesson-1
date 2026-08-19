base = float(input("Enter the number: "))
exponent = int(input("Enter the power (n): "))

result = 1

for i in range(exponent):
    result = result * base

print(f"{base} to the power {exponent} = {result}")