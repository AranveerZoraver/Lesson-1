class Pet:
    species_group = "Domestic Animal"

    def __init__(self, name, breed, age, owner):
        self.name = name
        self.breed = breed
        self.age = age
        self.owner = owner

    def display_profile(self):
        print("Pet Profile")
        print("-----------")
        print(f"Name: {self.name}")
        print(f"Breed: {self.breed}")
        print(f"Age: {self.age} years")
        print(f"Owner: {self.owner}")
        print(f"Group: {Pet.species_group}")
        print()


pet1 = Pet("Buddy", "Corgi", 3, "Aran")
pet2 = Pet("Luna", "German Shepherd", 5, "Sara")

pet1.display_profile()
pet2.display_profile()

print(pet1.name)
print(pet2.breed)