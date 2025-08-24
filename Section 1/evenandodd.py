# This program will ask you to enter the number and letting you know if is even or odd number

number = float(input("Enter the number: "))

if number % 2 == 0:
    print(f"{number} is an even number")
else:
    print(f"{number} is an odd number")
