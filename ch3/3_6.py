# Cracking the Coding Interview: 3.6
# Written by Josh Humphrey

class pet():

    def __init__(self,species,name):
        self.passed_count = 0
        self.species = species
        self.name = name

class animal_shelter():

    def __init__(self):
        self.dogs = []
        self.cats = []

    def adopt_dog(self):
        pet_to_adopt = self.dogs.pop(0)
        self.update_pet_tenure()
        return pet_to_adopt

    def adopt_cat(self):
        pet_to_adopt = self.cats.pop(0)
        self.update_pet_tenure()
        return pet_to_adopt

    def update_pet_tenure(self):
        for pupper in self.dogs:
            pupper.passed_count += 1
        for cat in self.cats:
            cat.passed_count += 1

    def adopt_oldest(self):
        old_cat = self.cats.pop(0)
        old_dog = self.dogs.pop(0)
        if old_dog.passed_count >= old_cat.passed_count:
            self.cats = [old_cat] + self.cats
            self.update_pet_tenure()
            return old_dog
        else:
            self.dogs = [old_dog] + self.dogs
            self.update_pet_tenure()
            return old_cat

    def enroll_pet(self, animal):
        if animal.species == "Dog":
            self.dogs.append(animal)
        else:
            self.cats.append(animal)


my_shelter = animal_shelter()
scruffy = pet("Dog","Scruffy")
tuna = pet("Cat","Tuna")
spot = pet("Dog","Spot")
fluffy = pet("Cat", "Fluffy")
my_shelter.enroll_pet(scruffy)
my_shelter.enroll_pet(tuna)
adopted_pet = my_shelter.adopt_oldest()
print(adopted_pet.name)
my_shelter.enroll_pet(spot)
my_shelter.enroll_pet(fluffy)
adopted_pet = my_shelter.adopt_cat()
print(adopted_pet.name)
adopted_pet = my_shelter.adopt_oldest()
print(adopted_pet.name)
