# ===== Section 1: Star Pyramid =====
print("Star Pyramid")
rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):
    for j in range(i):
        print("* ", end="")
    print()

# ===== Section 2: Floyd's Triangle =====
print("\nFloyd's Triangle")
rows2 = int(input("Enter the number of rows: "))

num = 1
for i in range(1, rows2 + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

# ===== Section 3: Diamond Pattern =====
print("\nDiamond Pattern")
rows3 = int(input("Enter the number of rows for the diamond: "))

# Upper half
for i in range(1, rows3 + 1):
    for s in range(rows3 - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()

# Lower half
for i in range(rows3 - 1, 0, -1):
    for s in range(rows3 - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()