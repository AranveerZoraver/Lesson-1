import random

secret = random.randint(1, 25)
attempts = 5
won = False

print("Welcome to number guessing game")
print("guess a specific number between 1 to 25 you have five attempts")

while attempts > 0 and not won:
    guess = int(input("enter your number: "))

    if guess == secret:
        print("Nice! You guessed the right number")
        won = True
    else:
        attempts -= 1

        difference = abs(secret - guess)

        if difference > 20:
            hint = "Frozen"
        elif difference > 10:
            hint = "cold"
        elif difference > 5:
            hint = "warm"
        else:
            hint = "hot"

        print(f"Wrong, hint: {hint}")
        for i in range(attempts):
            print("lives", end="")
        print("\n")


if not won:
    print(f"game lost, you ran out of attempts the scret number was {secret}.")