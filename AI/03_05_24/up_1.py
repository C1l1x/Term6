# 1.	    Напишете клас Rectangle с атрибути за дължина и ширина.

# 1.1.	Създайте метод Perimeter() за изчисляване на периметъра на правоъгълника и метод Area() 
# за изчисляване на площта на правоъгълника.

# 1.2.	Създайте метод display(), който показва дължината, ширината, периметъра и площта на обект, създаден с
# помощта на инстанция върху клас правоъгълник.



class Rectangle:
    x = 0
    y = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def Perimeter(self):
        return 2 * (self.x + self.y)
        
    def Area(self):
        return self.x * self.y
    
    def display(self):
        print(f"x: {self.x}")
        print(f"y: {self.y}")
        print(f"Perimeter: {Rectangle.Perimeter(self)}")
        print(f"Area: {Rectangle.Area(self)}")
        


z = Rectangle(5, 2)
z.display()