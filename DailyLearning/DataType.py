"""
Numeric Data Types
"""

Age=24 #integer (int) data type
print(Age)

CGPA=3.80 #Floating Point (float) data type
print(CGPA)

Complex_Number=24+3j #Complex number data type
print(Complex_Number)

"""
String Data Type
"""

Name="MD.SAZIB" #String Data type
print(Name)
"""
Sequence Data Type
"""

#List Data Type (Like Array but not exactly)
Name=["MD.SAZIB","Eva Kaji","Reyan"]
print(Name)
print("Index 0 : ",Name[0]," Index 2 : ",Name[2])

CGPA=[3.80,3.21,2.89]
print(CGPA)
print("Index 0 : ",CGPA[0]," Index 2 : ",CGPA[2])

Age=[24,21,22]
print(Age)
print("Index 0 : ",Age[0]," Index 2 : ",Age[2])

Mix=["MD.SAZIB",24,3.80]
print(Mix)
print("Index 0 : ",Mix[0]," Index 2 : ",Mix[2])

#Tuple Data Type

City=("Dhaka","Barishal","Gazipur")
print(City)
print("Index 0 : ",City[0]," Index 2 : ",City[2])

"""
List: Mutable, meaning you can change, add, or remove elements after the list is created.
Tuple: Immutable, meaning once a tuple is created, you cannot modify its contents.

# List
my_list = [1, 2, 3]
my_list[1]=5

# Tuple
my_tuple = (1, 2, 3)
# my_tuple[0] = 4  # This will raise an error

"""