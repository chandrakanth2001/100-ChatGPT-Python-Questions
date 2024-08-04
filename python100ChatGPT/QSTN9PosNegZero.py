# Write a Python program to check if a number is positive, negative, or zero.

def check(num):
    if num == 0:
        print(f"The number {num} is Zero")
    elif num > 0:
        print(f"The number {num} is Positive ")
    elif num < 0:
        print(f"The num {num} is negative ")

check(-80)