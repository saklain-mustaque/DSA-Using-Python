import math

class Person:
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age
    def show(self):
        return f'Name: {self.name}\nAge: {self.age}'
person = Person('Saklain','25')
print(person.show())


class Circle:
    def __init__(self, radius = None):
        self.radius = radius

    def get_radius(self):
        return self.radius
    
    def get_area(self):
        return math.pi * (self.radius**2)
    
    def get_circumference(self):
        return 2*math.pi*self.radius
circle = Circle(4)
print(circle.get_area())
print(circle.get_circumference())


class Team:
    def __init__(self):
        self.team_members = []
            
    def add_members(self):
        self.team_members.append(input("Enter the new member name:"))
    
    def display_members(self):
        n = int(input("Enter how many memebers you want to add:"))
        for n in range(n):
            self.add_members()
        if len(self.team_members) != 0:
            print("\n",("Team Members").center(40,'*'))
            for index, member in enumerate(self.team_members, start=1):
                print(index, member)
                
    
team = Team()
team.display_members()