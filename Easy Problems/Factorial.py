# Input: n = 5
# Output: 120
# Explanation: 5! = 5 * 4 * 3 * 2 * 1 = 120

# Input: n = 4
# Output: 24
# Explanation: 4! = 4 * 3 * 2 * 1 = 24

#[Approach - 1] - Iterative Solution O(n) Time and O(1) Space
def factorial(n):
    ans = 1
    i = 2
    #calculating the factorial
    while (i <= n):
        ans *= i
        i += 1
    return ans

#[Another Approach]- Recursive Solution O(n) Time and O(n) Space
def factorialRecursion(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


num = 5
print(factorial(num))
print(factorialRecursion(num))