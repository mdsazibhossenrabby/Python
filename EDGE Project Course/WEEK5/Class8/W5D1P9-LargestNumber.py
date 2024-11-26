

numbers=[i*3 for i in range(1,11)]

maximum=0

for i in numbers:
    if(maximum<i):
        maximum=i
print(f"The max value : {maximum}")