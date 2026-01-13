#[Naive Approach] - Adding One By One - O(n) Time and O(1) Space

def sumOfSquares(num):
    sum1=0
    for i in range(1,num+1):
        sum1=sum1+i**2
    print("Sum of Squares = ",sum1)
    
#[Expected Approach]- Using Mathematical Formulae - O(1) Time and O(1) Space

def FormulaSum(n):
     return (n*(n+1)*(2*n+1))//6


sumOfSquares(10)
print("Total FormulaSum = ",FormulaSum(10))