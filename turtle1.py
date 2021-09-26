import turtle

screen = turtle.getscreen()
t = turtle.Turtle()

class DrawShape:
    def draw(self, sides, angle):
        for distance in sides:
            t.forward(distance)
            t.left(angle)


class Triangle(DrawShape):
    def __init__(self, sides):
        self.sides = sides
        self.angle = 120
# x = 1
# for i in range(0, 40):
#     t.forward(100)
#     t.left(10)
#     t.back(102)
class HouseOfDream:
    def draw(self, sides, angle):
        for distance in sides:
            t.forward(distance)
            t.right(angle)
    def __init__(self, sides):
        self.sides = sides
        self.angle = 90
triangle = Triangle([100]*3)
triangle.draw (triangle.sides, triangle.angle)
house = HouseOfDream([100]*4)
house.draw (house.sides, house.angle)
t.right(90)
t.forward(100)
t.left(90)
t.forward(20)
class Door(DrawShape):
    def __init__(self, sides):
        self.sides = sides
        self.angle = 90 
door = Door([20]*4)
door.draw(door.sides, door.angle)
screen.mainloop()

class Triangle:
    pass

class Rectangle:
    pass

class HouseOfDream:
    def __init__(self, triangle, rectangle):
        self.roof = triangle
        self.body = rectangle
        self.door = rectangle

    def build_roof(self):
        self.roof.draw()

house = HouseOfDream(Triangle, Rectangle)

while not house:
    roof_status = house.build_roof()
