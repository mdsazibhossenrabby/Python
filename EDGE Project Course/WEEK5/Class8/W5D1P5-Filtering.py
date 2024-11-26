

numbers=[i for i in range(1,11)]

odds=list(filter(lambda x: x%2!=0,numbers))

print(f"The odd numbers are : {odds}")