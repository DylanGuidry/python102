#Numbers list
numbers = [78, -1, -1000, 9001, 201]
#Creat a new empy list so we can add things to it.
positive_numbers = []
#Loop over each number.
for num in numbers:
    #If number is positive.
    if num > 0:
        positive_numbers.append(num)
        #Add to new list.

#Output neww list.
print(positive_numbers)