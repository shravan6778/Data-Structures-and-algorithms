def toFindPrimeFactors(num):
    l = []
    i = 2
    temp = num # Using a temp variable is cleaner
    while temp > 1:
        if temp % i == 0:
            l.append(i)
            temp //= i
        else:
            i += 1
    return l

def toFindGCD(num1, num2):
    lnum1 = toFindPrimeFactors(num1)
    lnum2 = toFindPrimeFactors(num2)
    mul = 1
    
    # Use [:] to iterate over a copy of the list
    for i in lnum1[:]: 
        if i in lnum2:
            mul *= i
            lnum2.remove(i) # Remove from lnum2 so it's not reused
            lnum1.remove(i) # Remove from the original lnum1
            
    return mul

print(toFindGCD(36, 60)) 
# Output: 12

# Alternative
# def quick_gcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a

# print(quick_gcd(36, 60)) # Output: 12