#Functions:
def add(num1, num2):
    print("Adding numbers....")
    return num2 + num1

def add5(num):
    return add(num, 5)

user_num = int(input("What number would you like to add 5 to? "))

print(add5(user_num))

print(add(4, 6))
