
import random

numberToGuess=random.randint(1,100)
guess=None

while guess!=numberToGuess :
    guess=int(input("Enter a number between 1 to 100 : "))
    if guess>numberToGuess :
        print("Too High")
    elif guess<numberToGuess:
        print("Too Low")
print("Congratualtions! You have guessed the number ")
