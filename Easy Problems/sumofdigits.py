# Input: n = 687
# Output: 21
# Explanation: The sum of its digits are: 6 + 8 + 7 = 21

# Input: n = 12
# Output: 3
# Explanation: The sum of its digits are: 1 + 2 = 3

#[Approach 1] Digit Extraction - O(log10n) Time and O(1) Space
def sumOfDigits(n):
    sum1=0
    while(n!=0):
        rem1 = n % 10
        sum1 = sum1 + rem1
        n //= 10
    return sum1

#[Approach 2] Using Recursion - O(log10n) Time and O(log10n) Space
def sumOfDigitsRecursion(n):
    # Base Case
    if n == 0:
        return 0
    # Recursive Case
    return n % 10 + sumOfDigits(n // 10)

#[Approach 3] String Conversion
def sumOfDigitsSC(n):
    # Convert number to string
    s = str(n)
    sum = 0

    # Loop through each character, convert to digit, and add to sum
    for ch in s:
        sum += int(ch)

    return sum
print("Digit Extraction sum : ",sumOfDigits(12345))
print("Using Recursion sum : ",sumOfDigitsRecursion(12345))
print("String Conversion sum : ",sumOfDigitsSC(12345))


        