# Input:  n = 11
# Output: true

# Input:  n = 15
# Output: false

# Input:  n = 1
# Output: false 
import math
# School Method
def primeNumber(num):
    if num <= 1:
        return False
    for i in range(2,num):
        if(num%i==0):
            return False
            break
    return True

#Optimized School Method
def isPrime(n):
    if (n <= 1):
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if (n % i == 0):
            return False
    return True

print(f"School Method : {primeNumber(4)}")
print(f"School Optimized Method : {isPrime(4)}")