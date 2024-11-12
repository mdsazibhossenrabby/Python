

score=int(input("Enter your Score : "))

if score<=100 and score>=90:
    print("Grade A")
elif score<=89 and score>=80:
    print("Grade B")
elif score<=79 and score>=70:
    print("Grade C")
elif score<=69 and score>=60:
    print("Grade D")
elif score<60:
    print("Grade F")
else:
    print("Wrong Score")