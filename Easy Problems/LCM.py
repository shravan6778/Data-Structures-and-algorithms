# Input :  a = 10, b = 5
# Output :  10
# Explanation : 10 is the smallest number divisible by both 10 and 5

# Input :  a = 5, b = 11
# Output :  55
# Explanation : 55 is the smallest number divisible by both 5 and 11

#[Naive Approach] Using Conditional Loop

def lcmNative(a, b):
    g = max(a, b) 
    s = min(a, b)  
    for i in range(g, a * b + 1, g):
        if i % s == 0:
            return i
    return a * b 

#[Expected Approach] Using GCD LCM Formula
def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

def lcm(a, b):
    return (a // gcd(a, b)) * b

a = 10
b = 5
print(lcmNative(a, b))

a = 10
b = 5
print(lcm(a, b))