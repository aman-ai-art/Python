# This is a simple class to represent a human being with attributes and methods. The class has an initializer method to set the name and age of the person, and two methods to
class Human:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
    
    def talk(self):
        print(f'Hi, I am {self.name} and I am {self.age} years old.')
    
    def eat(self):
        print(f'{self.name} wants to eat something.')
    
person1 = Human('Aman', 20)
person2 = Human('Sabina', 19)
person1.talk()
person1.eat()
person2.talk()
person2.eat()