astring="Floccinaunici"

# lenght of string
print(f"The Length of the String is : {len(astring)}")

# checking the end of the string 
print(f"Is the string ends with 'rry' : {astring.endswith("rry")}")

# checking the start of the string 
print(f"Is the string strats with 'Fl' : {astring.startswith("Fl")}")

# return capitalized the first character of the string 
print(f"The Capital form of the string : {astring.capitalize()}")

# return uppercase characters 
print(f"The Uppercase of the string : {astring.upper()}")

# return lowercase characters 
print(f"The Lowercase of the string : {astring.lower()}")

# return the first index of a word from the string 
print(f"Find the index of word 'nau' : {astring.find("nau")}")