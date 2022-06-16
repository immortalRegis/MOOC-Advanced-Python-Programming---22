# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

class Room:
    def __init__(self):
        self.people = []
        self.total_height = 0

    def add(self, person: Person):
        self.people.append(person)
        self.total_height += person.height

    def is_empty(self):
        return len(self.people) == 0

    def print_contents(self):
        if len(self.people) > 0:
            print(f"There are {len(self.people)} people in the room, and their combined height is {self.total_height} cm")
            for person in self.people:
                print(f"{person.name} ({person.height} cm)")

    def shortest(self):
        if len(self.people) == 0:
            return None
        
        shortest = self.people[0]
        for i in range(len(self.people)):
            if self.people[i].height < shortest.height:
                shortest = self.people[i]
        
        return shortest
    
    def remove_shortest(self):
        if len(self.people) == 0:
            return None
        shortest_person = self.shortest()
        self.total_height -= shortest_person.height
        self.people.remove(shortest_person)
        return shortest_person

