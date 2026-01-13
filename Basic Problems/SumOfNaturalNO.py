#[Naive Approach] Using Loop - O(n) Time and O(1) Space
def NativeSum(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
    print("Total Sum = ",sum)
    
#[Alternative Approach] Using Recursion -O(n) and O(n) Space
def RecursiveSum(n):
    if(n==1):
        return 1
    return n + RecursiveSum(n-1)

#[Expected Approach] Formula Based Method- O(1) Time and O(1) Space
def FormulaSum(n):
    return (n*(n+1))//2




NativeSum(90)
print("Total RecursiveSum = ",RecursiveSum(90))
print("Total FormulaSum = ",FormulaSum(90))
