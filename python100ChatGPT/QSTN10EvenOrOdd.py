# Write a Python program to check if a number is even or odd.

def evenOrodd(num):
    if num %2 == 0:
        print(f"The num {num} is even")
    elif num %2 != 0:
        print(f"The num {num} is odd")

evenOrodd(50)
evenOrodd(63)