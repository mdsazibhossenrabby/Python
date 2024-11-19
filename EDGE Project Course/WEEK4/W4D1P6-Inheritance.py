

class Animal:
    def sound(self):
        print("Animal Sound")
        
class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")
        

dog=Dog()
dog.sound()

cat=Cat()
cat.sound()