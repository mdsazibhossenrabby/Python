
text=input("Enter A string : ").lower()
count=0
for char in text:
    if char in 'aeiou':
        count+=1
print(f"There are {count} vowels in the string")
