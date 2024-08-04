#Write a Python program to convert kilometers to miles.


def kmTomiles(km):
    print(f"{km}Kms")
    toMiles = km * 0.621371
    print(f"{km}kms is equal to {round(toMiles)} miles")

kmTomiles(576)