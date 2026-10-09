from array import array

box1 = {"apple", "biscuit", "juice", "cookie"}
box2 = {"juice", "cookie", "banana", "chips"}

print("Box 1:", box1)
print("Box 2:", box2)

box1.add("banana")
print("Box 1 after adding banana:", box1)

shared = box1.intersection(box2)
print("Shared snacks:", shared)

snack_counts = array("i", [3, 5, 2, 5, 4])
print("Snack counts:", snack_counts)

snack_counts.insert(1, 10)
print("After insert:", snack_counts)

snack_counts.append(5)
print("After append:", snack_counts)

print("Times 5 appears:", snack_counts.count(5))

snack_counts.reverse()
print("Reversed array:", snack_counts)