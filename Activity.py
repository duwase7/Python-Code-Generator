name = input("What is your name?")
age = input("How old are you?")
color = input("What is your favourite color?")
print(f"your name is {name} your age is {age} years old your favourite color is {color}")


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
sum = num1 + num2
multiplication = num1 * num2
subtraction = num1 - num2
division = num1 / num2
print(f"The sum of {num1} + {num2} = {sum}.")
print(f"The multiplication of {num1} * {num2} = {multiplication}.")
print(f"The subtraction of {num1} - {num2} = {subtraction}.")
print(f"The division of {num1} / {num2} = {division}.")


n = int(input("Enter the number: "))
if n % 2 == 0:
    print(f"The even number is {n}.")
else:
    print(f"The odd number is {n}.")
print("Numbers from 1 to 20 are:")
for i in range(1, 20):
    print(i, end=" ")

print("\nEven numbers from 1 to 20 are:")
for i in range(1, 21):
    if i % 2 == 0:
        print(i, end=" ")


favourite_food = []
print(f"Your 5 favourite foods are:" )
for i in range(5):
    favourite_food.append(input())
print(f"Your favourite foods in reverse order")
for food in reversed(favourite_food):
    print(food)


food_hate = []
print(f"The 4 foods you hate are:")
for i in range(4):
    food_hate.append(input())
if food_hate
    print(f"The food you hate are in reverse order: {food_hate}")
else food_hate
    print(f"The food you hate are in reverse order: {food_hate}")
food_hate = []
print(f"The 4 foods you hate are:")
for i in range(4):
    food_hate.append(input())
if food_hate
    print(f"The food you hate are in reverse order: {food_hate}")


print("Hello world")
name = input("What is your name?")
age = input("How old are you?")
color = input("What is your favourite color?")
print(f"Your name is {name}.")
print(f"Your age is {age}."


