# Write a Python program to convert Celsius to Fahrenheit.

def celToFahren(cel):
    print(f"{cel}celsius")
    toFahren = (cel*9/5)+32
    print(f"{cel}celsius is equal to {toFahren}Fahrenheit")

celToFahren(50)