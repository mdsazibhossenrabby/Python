

try :
    result=10/0
except ZeroDivisionError as Err:
    print(f"Error is : {Err}")

n=int(input("Enter Divider number : "))
try :
    result=10/n
    print(result)
except ZeroDivisionError as Err:
    print(f"Error is : {Err}")
    