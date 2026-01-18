# Input : a1 = 2,  a2 = 3,  n = 4
# Output : 5
# Explanation : The series is 2, 3, 4, 5, 6, ....   , thus the 4th term is 5. 

# Input : a1 = 1, a2 = 3, n = 10
# Output : 19
# Explanation:  The series is: 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21..... Thus,10th term is 19.

#[Naive Approach] - Using for Loop
def nthTermOfAP(a1, a2, n):
    nthTerm = a1
    d = a2 - a1
    for i in range(1, n):
        nthTerm += d
    return nthTerm

#[Expected Approach] - Using the Formula for nth Term

def nthTermOfAPExpected(a1, a2, n):
    # using formula to find the
    # Nth term t(n) = a(1) + (n-1)*d
    return a1 + (n - 1) * (a2 - a1)


a1 = 2
a2 = 3
n = 4
print("Native Approach:",nthTermOfAP(a1, a2, n))
print("Expected Approach:",nthTermOfAPExpected(a1, a2, n))