# Cracking the Coding Interview: 16.10
# Written by Josh Humphrey
import random

class Person():

    def __init__(self, birth, death):
        self.birth = birth
        self.death = death

def generate_people(population):
    population_array = []
    for i in range(population):
        birth = random.randint(1900,1950)
        death = random.randint(1951,2000)
        population_array.append(Person(birth,death))
    return population_array

population_data = generate_people(10000)

def find_most_alive(population_data):
    max_alive = 0
    max_year = None
    for year in range(1900, 2000):
        year_count = 0
        for i in range(len(population_data)):
            person = population_data[i]
            if person.birth < year and person.death > year:
                year_count += 1
        if year_count > max_alive:
            max_alive = year_count
            max_year = year
    return [max_year, max_alive]

result = find_most_alive(population_data)
print("In the year " + str(result[0]) + " there were " + str(result[1]) + " alive!")

def faster_find_most_alive(population_data):
    birth_array = []
    death_array = []
    for p in population_data:
        birth_array.append(p.birth)
        death_array.append(p.death)
    births = sorted(birth_array)
    deaths = sorted(death_array)
    max_alive = 0
    max_year = None
    current_alive = 0
    for year in range(1900,2000):
        for birth_year in birth_array:
            if birth_year == year:
                current_alive += 1
        for death_year in death_array:
            if death_year == year:
                current_alive -= 1
        if current_alive > max_alive:
            max_year = year
            max_alive = current_alive
    return [max_year, max_alive]

result = faster_find_most_alive(population_data)
print("In the year " + str(result[0]) + " there were " + str(result[1]) + " alive!")
