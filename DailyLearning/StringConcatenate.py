#String Concatenate
name = "MD.SAIZB "
concatenateName=name+name
print(f"Normal Concatenated String : {concatenateName}")


#String Concatenate using join() method
name1 = "MD.SAIZB "
name2="Hossen "
name3="Rabby "
join1=name1.join([name2,name3])
join2="My name is ".join([name1,name2,name3])
join3="My name is ".join([name1,name2,name3])+", I am 24 Years old"
print(f"String Join 1 : {join1}")
print(f"String Join 2 : {join2}")
print(f"String Join 3 : {join3}")



#String Concatenate using format() method
Format1="{} {} .".format("I am",name1)
Format2="My name is {} {} {} .".format(name1,name2,name3)
Format3="I am {} {} ".format(name1,name2)+", I am 24 Years old"
print(f"String formate 1 : {Format1}")
print(f"String Format 2 : {Format2}")
print(f"String format 3 : {Format3}")


#String Concatenate using % formating
modFormat1="%s %s ."%("I am",name1)
modFormat2="My name is %s %s %s ."%(name1,name2,name3)
modFormat3="I am %s %s "%(name1,name2)+", I am 24 Years old"
print(f"String Modulous formate 1 : {modFormat1}")
print(f"String Modulous Format 2 : {modFormat2}")
print(f"String Modulous format 3 : {modFormat3}")




#String Concatenate with repetition
RepeatName=name*5
print(f"Repeat Concatenated String : {RepeatName}")