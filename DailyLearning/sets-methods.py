marks={1,2,45,78,7,7,7.54,7.54,22,3,"Sazib"}
#Add at last
marks.add(666)
print(marks)
#Remove Element
marks.remove(3)
print(marks)

#Remove randome element from set
marks.pop()
print(marks)

#set union
s1={1,2,3,4}
s2={2,4,5,6,7}

print(f"Set union : {s1.union(s2)}")
print(f"Set intersection : {s1.intersection(s2)}")
