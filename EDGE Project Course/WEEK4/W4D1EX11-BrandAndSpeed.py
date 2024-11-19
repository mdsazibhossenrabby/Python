
from time import sleep



class Vehicle :

    def __init__(self,brand,speed=0):
        self.brand=brand
        self.speed=speed

    def accelarate(self,amount):
        self.speed+=amount
        print(f"The speed increases to {self.speed}")

    def braker(self,amount):
        self.speed=max(0,self.speed-amount)
        print(f"The speed decreased to {self.speed}")


car=Vehicle("Toyota",50)
car.accelarate(100)
car.braker(50)