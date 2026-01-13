#Iterative Approach
def printTable(num):
    for i in range(1,11):
        print(f"{num} * {i} = {num*i}")
    print()   
#Recursive Approach
def RecursiveApproach(num,i=1):
    if(i==11):
        return
    print(f"{num} * {i} = {num*i}")
    i=i+1
    RecursiveApproach(num,i)

printTable(2)
RecursiveApproach(5)