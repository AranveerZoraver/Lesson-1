homework = ["Math", "Science", "History", "Art"]
tasks_remaining = len(homework)

while tasks_remaining > 0:
    current_task = homework[len(homework) - tasks_remaining]
    status = input(f"Have you finished '{current_task}'? (yes/no): ")

    if status.lower() == "yes":
        print(f"'{current_task}' marked complete!")
        tasks_remaining -= 1
    else:
        print(f"'{current_task}' still pending, checking again...")

print("All homework complete! Great job.")


checks = 0

while True:
    checks += 1
    print(f"Automated check #{checks}...")

    if checks == 5:
        print("Reached safety limit, stopping with break.")
        break