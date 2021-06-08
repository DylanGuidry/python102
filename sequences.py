# Strings
string = "example"
empty_string = ""
print(string[3])

#Integers
7

#Floats
7.7

#Booleans
True
False

#Newly Added:

#List
#Every list has an index: starting at 0.
languages = ["python", "javascript", "html", "css"]
empty_list = []
#You can print lists and/or access items by index:
print(languages[2])

#Accessing items outside of possible values will throw an IndexError
print(languages[10])

#When starting with negatives it will loop and read from the right
print(languages[-1]) #prints CSS


languages = ["python", "javascript", "html", "css"]
index = 0
while index < len(languages):
    print("No, " + languages[index] + "is the best.")
    index += 1

#For loops
for lang in languages:
    print("No, " + lang + " is the best language.")