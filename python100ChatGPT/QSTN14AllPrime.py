import math


#Checking
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

#Printing

def printPrime(start,end):
    for num in range(start,end+1):
        if is_prime(num):
            print(num,end=" ")

    print()

start = int(input("Enter the start of the interval: "))
end = int(input("Enter the end of the interval: "))

print(f"Prime numbers between {start} and {end} are:")
printPrime(start, end)