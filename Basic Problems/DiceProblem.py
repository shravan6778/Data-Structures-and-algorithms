# Input: n = 2
# Output: 5
# Explanation: For dice facing number 5 opposite face will have the number 2.

# Input: n = 6
# Output: 1
# Explanation: For dice facing number 6 opposite face will have the number 1.

# [Naive Approach] Using if-else Statement

def oppositeFaceOfDice(n):
    ans=0
    if(n == 1):
        ans = 6
    elif(n == 2):
        ans = 5
    elif(n == 3):
        ans = 4
    elif(n == 4):
        ans = 3
    elif(n == 5):
        ans = 2
    else:
        ans = 1
    
    return ans

#[Expected Approach] Using Sum of Two Sides
def oppositeFaceOfDiceExpected(n):
    # Stores number on opposite face
    # of dice
    ans = 7 - n
    return ans

n = 2
print("Native Approach:",oppositeFaceOfDice(n))
print("Expected Approach:",oppositeFaceOfDiceExpected(n))