# This code defines a class called Newtype with an initializer that takes two parameters, x and y, and assigns them to instance variables. The class also has two methods, move and draw, which print messages when called. The code then creates an instance of Newtype called Point with specific coordinates, calls the move method, and prints the coordinates. Finally, it creates another instance called Type and prints its coordinates as well.
class Newtype:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print('Moving')
    
    def draw(self):
        print("Drawing")

Newtype.x = 1
Newtype.y = 2
print(f'coordinates: ({Newtype.x}, {Newtype.y})')
Point = Newtype(100, 200)
Point.move()
Point.x = 300
print(f'coordinates: ({Point.x}, {Point.y})')
Point.draw()
Type = Newtype(10, 20)
print(f'coordinates: ({Type.x}, {Type.y})')
