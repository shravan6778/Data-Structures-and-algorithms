#[Naive Approach] Using Third Variable
def swapNumbers():
    a=10
    b=20
    temp=0
    #swap logic
    temp=a
    a=b
    b=temp
    print(f"a={a} b={b}")
    
#[Expected Approach] Without using Third Variable
def ExpectedSwap():
    a=10
    b=20
    total = a+b
    #swap withot third variable
    a=b
    b=total-a
    print(f"Without Third variable a={a} b={b}")

#[Alternate Approach] Built-in Swap
def AlternativeApproach():
    a = 2
    b = 3
    print("a =", a, " b =", b)
    # Tuple unpacking
    a, b = b, a
    print(f"Alternative Approach a={a} b={b}")

swapNumbers()
ExpectedSwap()
AlternativeApproach()