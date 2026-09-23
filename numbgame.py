import random
playing = True
number = str(random.randint(0,9))
print("i will generate a number from 0 to 9 and you will have to gues the number one digit one.")
print("the game end when you get 1 hero!")
while playing:
    guess = input("give me you best guess! \n")
    if number == guess:
        print("you win the game")
        print("the number was",number)
        break

    else:
        print("you guess isnt quite right try again \n") 