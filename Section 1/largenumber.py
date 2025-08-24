# This program will ask you to enter 2 numbers and will let you know which one is large and which one is small

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

if number1 > number2:
    print(f"{number1} is the largest number entered")
else:
    print(f"{number2} is the largest number entered")

if number1 == number2: 
    print("Both numbers are equal")
