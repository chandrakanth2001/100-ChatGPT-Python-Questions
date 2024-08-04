# Write a Python program to check if a year is a leap year.

def checkLeapyear(year):
    if year %4 == 0:
        if year %100 == 0:
            if year %400 == 0:
                print(f"The year {year} is a Leap Year")
            else:
                print(f"The year {year} is not a Leap Yea")
        else:
            print(f"The year {year} is a Leap Year")
    else:
        print(f"The year {year} is not a Leap Year")

checkLeapyear(2028)