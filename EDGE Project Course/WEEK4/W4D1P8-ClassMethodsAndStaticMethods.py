PI=3.1416
class Circle:

    def Area(self,r):
        return PI*r**2
    
    @staticmethod
    def Radius(d):
        return d/2
    
    @classmethod
    def display(cls):
        print("Class Method")

c=Circle()

print(Circle.Radius(10))

print(c.Area(Circle.Radius(10)))

Circle.display()