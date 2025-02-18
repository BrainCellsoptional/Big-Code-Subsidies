class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
 
    def introduce(self):
        return f"Hi, my name is {self.name}. I am {self.age} years old."
 
    def greet(self, other_person):
        return f"Hello, {other_person.name}! Nice to meet you."