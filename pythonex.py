#Finding the sum:
numbers = [1, 2, 3, 4, 5]
print(sum(numbers))

#Finding the largest number:
numbers = [1, 50, 92, 91048, 492]
highest_number = 0
for num in numbers:
    if num > highest_number:
        highest_number =num

print(highest_number)

#Finding the smallest number:
number = [2, 1, 3, 4, 5]
smallest = 5
for num in number:
    if num < smallest:
        smallest = num
print(smallest)

#Finding even numbers:
numbers = [30, 45, 57, 67, 51]
even_number = 0
for num in numbers: