sentence="I am feeling good"
#Positive Indexing
print("Positive Indexing")
print(sentence[3])
print(sentence[1])
print(sentence[0])

#Negetive Indexing
print("Negative Indexing")
print(sentence[-1])
print(sentence[-2])
print(sentence[-4])

#String Slicing
print("String \"Start\" \"Stop\" slicing [start index:stop position]")
print(sentence[0:3])
print(sentence[:6])
print(sentence[2:6])
print(sentence[2:])
print("String \"Step\" slicing [start index::step number]")
print(sentence[0::3])
print(sentence[2::2])