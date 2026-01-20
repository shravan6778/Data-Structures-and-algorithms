# Input: n = 122
# Output: 221
# Explanation: By reversing the digits of number, number will change into 221.

# Input: n = 200
# Output: 2
# Explanation: By reversing the digits of number, number will change into 2.

# Input: n = 12345 
# Output: 54321
# Explanation: By reversing the digits of number, number will change into 54321.

#Using Recursion
def reverseDigitsRecurion(n, revNum, basePos):
    if n > 0:
        reverseDigitsRecurion(n // 10, revNum, basePos)  
        revNum[0] += (n % 10) * basePos[0]       
        basePos[0] *= 10 

#Using String
def reversDigitsString(n):
    s = str(n)
    s = list(s)
    s.reverse()
    s = ''.join(s)
    n = int(s)
    return n

#Using String and Slicing in Python
def reversDigitsSlicing(n):
    s = str(n)
    s = s[::-1]
    n = int(s)
    return n

n = 4562
rev = 0
while(n > 0):
    a = n % 10
    rev = rev * 10 + a
    n = n // 10
print("Reversing Digit by Digit : ",rev)

                        
n = 4562
revNum = [0]  
basePos = [1]  
reverseDigitsRecurion(n, revNum, basePos)
print("Using Recursion : ",revNum[0])

num = 4562
print("Using String : ",reversDigitsString(num))

n = 4562
print("Using String and Slicing in Python : ",reversDigitsSlicing(n))