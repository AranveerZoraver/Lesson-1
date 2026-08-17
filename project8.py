holiday_type = input("What type of holiday do you want? (beach/mountain/city): ").strip().lower()

if holiday_type == "beach":
    mood = input("Do you want relaxation or adventure? (relaxation/adventure): ").strip().lower()

    if mood == "relaxation":
        print("Your plan: Spend the day sunbathing and reading by the shore.")
    else:
        print("Your plan: Try surfing and snorkeling for an adventurous beach day.")

elif holiday_type == "mountain":
    activity = input("Do you prefer hiking or skiing? (hiking/skiing): ").strip().lower()

    if activity == "hiking":
        print("Your plan: Trek through scenic mountain trails.")
    else:
        print("Your plan: Hit the slopes for a day of skiing.")

elif holiday_type == "city":
    interest = input("Are you interested in culture or shopping? (culture/shopping): ").strip().lower()

    if interest == "culture":
        print("Your plan: Visit museums and historic landmarks.")
    else:
        print("Your plan: Explore local markets and boutiques.")

else:
    print("Sorry, that's not a recognised holiday type. Please choose beach, mountain, or city.")