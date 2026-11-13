scores = {
    "Aisha": 85,
    "Ben": 72,
    "Carla": 91,
    "David": 64,
    "Emma": 78
}

total = 0
for score in scores.values():
    total = total + score
average = total / len(scores)
print("Class average:", average)

top_name = ""
top_score = 0
for name in scores:
    if scores[name] > top_score:
        top_score = scores[name]
        top_name = name
print("Top scorer:", top_name, "with", top_score)

search = input("Enter a student name: ")
result = scores.get(search)
if result is None:
    print("Student not found")
else:
    print(search, "scored", result)