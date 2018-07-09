# Cracking the Coding Interview: 17.8
# Written by Josh Humphrey

people = [(65, 100),(70, 150),(56, 90),(75, 190),(60, 95),(68, 110)]

def create_tower(people):
    available = people
    HEIGHT = 0
    WEIGHT = 1
    tallest_person = people[0]
    for i in range(1, len(people)):
        if people[i][HEIGHT] > tallest_person[HEIGHT]:
            tallest_person = people[i]
    available.remove(tallest_person)
    tower = [tallest_person]
    for i in range(1, len(available)):





result = create_tower(people)
print(result)
