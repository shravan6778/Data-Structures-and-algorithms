# Input :  a = 7, b = 10, c = 5 
# Output : Valid
# We can draw a triangle with the given three edge lengths.

# Input : a = 1, b = 10, c = 12 
# Output : Invalid
# We can not draw a triangle with the given three edge lengths.

def checkValidity(a, b, c): 
    if (a + b <= c) or (a + c <= b) or (b + c <= a) :
        return False
    else:
        return True        

a = 7
b = 10
c = 5
if checkValidity(a, b, c):
    print("Valid") 
else:
    print("Invalid")