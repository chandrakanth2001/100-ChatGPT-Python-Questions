# Write a Python program to find the largest among three numbers.

num1 = int(input("Enter the first no: "))
num2 = int(input("Enter the second no: "))
num3 = int(input("Enter the third no: "))

if num1 >= num2 and num1 >= num3:
    print(f"{num1} is the largest")
elif num2 >= num1 and num2 >= num3:
    print(f"{num2} is the largest")
else:
    print(f"{num3} is the largest")
