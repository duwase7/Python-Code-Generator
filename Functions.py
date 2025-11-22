def add(a, b):
    return a + b
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
result = add(num1, num2)
print(f"The sum of {num1} and {num2} is {result}")
def check_even_odd(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
num = int(input("Enter a number: "))
check_even_odd(num)
def greet_user(name):
    print(f"Hello {name} Welcome to my Python activity")
greet_user("Olivier")
greet_user("Tiffany")
greet_user("Davine")
def find_largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
print(f"Largest number is {find_largest(5, 6, 7)}.")
def multiplication_table(number):
    print(f"The multiplication table for {number}:")
    for i in range(1, 11):
        print(f"{number} * {i} = {number * i}")
multiplication_table(4)



