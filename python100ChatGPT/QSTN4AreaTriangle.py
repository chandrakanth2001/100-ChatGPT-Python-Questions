# Write a Python program to find the area of a triangle.

def triArea():
    b = int(input("Enter base: "))
    h = int(input("Enter height: "))
    area = 1/2 * b * h
    print(f"Area is : {round(area)}")

triArea()