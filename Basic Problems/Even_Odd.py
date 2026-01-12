#[Naive Approach] By Finding the Remainder - O(1) Time and O(1) Space
def check_even_odd(num):
    if(num%2==0):
        print(f"The number {num} is even")
    else:
        print(f"The number {num} is odd")
        
        
#[Efficient Approach] Using Bitwise AND Operator - O(1) Time and O(1) Space
def EfficientApproach(num):
    if(num&1)==0:
        return True
    else:
        return False
    
if EfficientApproach(717199):
    print("EfficientApproach:Even Number")
else:
    print("EfficientApproach:Odd Number")
check_even_odd(23450986)