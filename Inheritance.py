# Inheritance in Python allows a new class (called a child class) to inherit attributes and methods from an existing class (called a parent class). This promotes code reusability and establishes a natural hierarchical relationship between classes. In this example, we have a parent class called 'cat' with methods 'climb' and 'run'. The 'lion' and 'tiger' classes are child classes that inherit from the 'cat' class. The 'lion' class has an additional method 'roar', while the 'tiger' class has an additional method 'hunt'.
class cat:
    def climb(self):
        print("The cat is climbing.")
    
    def run(self):
        print("The cat is running.")

class lion(cat):
    def roar(self):
        print("The lion is roaring.")

class tiger(cat):
    def hunt(self):
        print("The tiger is hunting.")
    
cat1 = cat()
cat1.climb()
cat1.run()
lion1 = lion()
lion1.climb()
lion1.roar()
tiger1 = tiger()
tiger1.run()
tiger1.hunt()
