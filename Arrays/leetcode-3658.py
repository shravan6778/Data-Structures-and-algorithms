'''
Input: n = 4

Output: 4

Explanation:

Sum of the first 4 odd numbers sumOdd = 1 + 3 + 5 + 7 = 16
Sum of the first 4 even numbers sumEven = 2 + 4 + 6 + 8 = 20
Hence, GCD(sumOdd, sumEven) = GCD(16, 20) = 4.'''

def gcdOfOddEvenSums(n: int) -> int:
    sumOdd=1
    sumEven=2
    rem=0
    for i in range(1,n+1):
        sumOdd+=2
        sumEven+=2
    while sumEven!=0:
        rem=sumEven%sumOdd
        sumOdd=sumEven
        sumEven=rem
    return sumOdd

        