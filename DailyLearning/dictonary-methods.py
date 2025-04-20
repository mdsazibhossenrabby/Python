marks={
    "Sazib":90,
    "Eva":88,
    "Kazi":79,
    "List":[1,100,2,200],
    1101:"Rabby"
}
print(f"items : {marks.items()}")
print(f"Keys : {marks.keys()}")
print(f"Values : {marks.values()}")
#Update Value
marks.update({"Kazi":80})
# Add Items
marks.update({"Rabby":"good Boy"})
print(marks)
#get returened value
print(f"The Value of 1101 : {marks.get(1101)}")