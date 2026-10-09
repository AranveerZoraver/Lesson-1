marks = [78, 85, 92, 67, 88, 74, 95]

print("Marks:", marks)
print("Number of students:", len(marks))

print("First mark:", marks[0])
print("Last mark:", marks[-1])
print("Second to last mark:", marks[-2])

print("First three marks:", marks[0:3])
print("Last three marks:", marks[-3:])

total = 0
smallest = marks[0]
largest = marks[0]

for mark in marks:
    total += mark
    if mark < smallest:
        smallest = mark
    if mark > largest:
        largest = mark

average = total / len(marks)

print("Total:", total)
print("Average:", round(average, 2))
print("Smallest:", smallest)
print("Largest:", largest)