

class Ractagle :
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        return self.length*self.width

    def perimeter(self):
        return 2*(self.length+self.width)

rect=Ractagle(10,5)

print(f"The Area is : {rect.area()}")
print(f"The Parimeter is : {rect.perimeter()}")