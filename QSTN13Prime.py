#One way
import math

num = int(input("Enter the num to be checked for prime or not: "))

# if num < 2:
#     print("Not a Prime")
# for i in range(2,num):
#     if num %i == 0:
#         print(f"The num {num} is not a Prime ")
#         break
# else:
#     print(f"The num {num} is a Prime :")
#

#Efficient way

def checkPrime(num):
    if num < 2:
        return False

    for i in range(2,int(math.sqrt(num))+1):
        if num %i == 0:
            return False

    return True

if checkPrime(num):
    print(f"The num {num} is a Prime")
else:
    print(f"The num {num} is not a Prime")
