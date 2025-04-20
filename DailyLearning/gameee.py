import random

guess=int(random.random()*10)
count=0
chanches=3
while (True):
    guessed=int(input("Enter Your Number (0 to 10): "))
    count+=1
    chanches-=1
    if(guess==guessed):
        print("Hurray --- Welcome You guessed right !")
        break
    elif(count==3):
        print("Sorry You have no Chances to Play . \n---End---")
        break
    elif(guess>guessed):
        print(f"Your Guess is very low. Try Again ----- You have {chanches} life")
    elif(guess<guessed):
        print(f"Your Guess is very high. Try Again ----- You have {chanches} life")