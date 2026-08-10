print("welcome to ride builder")

print("step 1: pick your vehicle")
print("   1 bicycle")
print("   2 motorbike")
print()

choice = int(input("enter 1 or 2"))

if choice == 1:
    print("step 2 pick your bicycle")
    print("   1 racing bike")
    print("   2 mtn bike")
    print()

    bike_type = int(input("enter 1 or 2"))
    print()

    if bike_type == 1:
        print("you picked racing bike")
        print("top speed 120 kmh")
        print("best for racing tracks")
    else:
        print("you picked mtn bike")
        print("top speed 65kmh")
        print("best for mountain and dirt tracks")

elif choice == 2:
    print("Step 1: pick your car type")
    print("   1 - sedan")
    print("   2 - musclecar")
    print()

    car_type = int(input("enter 1 or 2:  "))
    print()

    if car_type == 1:
        print("you picked  : Sedan")
        print("seats       : 5 passengers")
        print("best for    : family trips")
    else:
        print("you picked  : musclecar")
        print("seats       : 4 passengers")
        print("best for    : drag racing")

else:
    print("that is not a valid choice, press either 1 or 2")

