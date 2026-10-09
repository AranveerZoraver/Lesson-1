habit = ("Exercise", 30, True)
week = (1, 0, 1, 1, 0, 1, 1)

print("Habit:", habit)
print("Weekly record:", week)

print("Items in habit tuple:", len(habit))
print("Days tracked:", len(week))

print("Habit name:", habit[0])
print("Last day:", week[-1])

print("First three days:", week[0:3])
print("Weekend (last two days):", week[-2:])

try:
    week[0] = 5
except TypeError as error:
    print("Cannot change a tuple:", error)

extended_week = week + (1,)
print("New tuple with extra day:", extended_week)
print("Original is unchanged:", week)