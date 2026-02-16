# Input :  a = 10, b = 5
# Output :  10
# Explanation : 10 is the smallest number divisible by both 10 and 5

# Input :  a = 5, b = 11
# Output :  55
# Explanation : 55 is the smallest number divisible by both 5 and 11

#[Naive Approach] Using Conditional Loop

def lcmNative(a, b):
    r=1
    i=2
    while a>1 or b>1:
        if a%i==0 or b%i==0:
            r*=i
            if a%i==0:
                a//=i
            if b%i==0:
                b//=i
        else:
            i += 1
    return r


#[Expected Approach] Using GCD LCM Formula
def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

def lcm(a, b):
    return (a // gcd(a, b)) * b

a = 16
b = 28
print(lcmNative(a, b))

a = 16
b = 28
print(lcm(a, b))