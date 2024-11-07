
fruites=["apple","banana","cherry","date","elderberry"]
print(f"Fruit list : {fruites}")
#Access First Furit
print(f"First Fruit : {fruites[0]}")

#Access Last Furit
print(f"Last Fruit : {fruites[-1]}")

#Add New Fruit
fruites.append("pineapple") #add at last
print(f"Updated Fruit list : {fruites}")

#Remove Item
fruites.pop(0) #index 1 item will be removed
print(f"Fruit list after removal: {fruites}")
