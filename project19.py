import random
import math


def generate_lucky_number():
    return random.randint(1, 100)


def choose_activity():
    activities = [
        "Read a chapter of a book",
        "Go for a 15-minute walk",
        "Try a new recipe",
        "Watch a documentary",
        "Learn 5 words in a new language",
        "Call an old friend",
        "Sketch something you see around you",
    ]
    return random.choice(activities)


def play_guessing_game(target, max_attempts=7):
    attempts = 0
    total_distance = 0

    print(f"\nI'm thinking of your lucky number (1-100). You have {max_attempts} tries.")

    while attempts < max_attempts:
        guess = int(input("Your guess: "))
        attempts += 1

        if guess == target:
            print(f"Correct! You got it in {attempts} attempt(s).")
            return attempts

        distance = math.fabs(guess - target)
        total_distance += distance
        direction = math.copysign(1, target - guess)
        hint = "higher" if direction > 0 else "lower"
        print(f"Not quite, try {hint}.")

        average_distance = total_distance / attempts
        print(f"Average distance so far: between {math.floor(average_distance)} and {math.ceil(average_distance)}.")

        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"{remaining} attempt(s) left.")

    print(f"Out of attempts. The lucky number was {target}.")
    return attempts


def main():
    print("=== Random Fun Calculator ===")

    lucky_number = generate_lucky_number()
    activity = choose_activity()

    print(f"\nYour lucky number: {lucky_number}")
    print(f"Your random activity: {activity}")

    attempts_used = play_guessing_game(lucky_number)

    shared_factor = math.gcd(lucky_number, attempts_used)
    print(f"\nGCD of your lucky number and attempts used: {shared_factor}")


if __name__ == "__main__":
    main()