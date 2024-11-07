
sentence="Learning Python is fun!"
#positive slicing
slice1=sentence[9:15]
slice2=sentence[19:22]
#negative slicing
slice3=sentence[-4:-1] #fun , -1 including,-4 excluding,extra character at last

#Step Slicing
slice4=sentence[0:15:3] #slice string by stepping 2 characters


print(f"Substring 1 : {slice1}")  #start index: including, end index: excuding
print(f"Substring 2 : {slice2}")
print(f"Substring 3(Negative Slicing): {slice3}")
print(f"Substring 4(Step Slicing): {slice4}")
