#input : [1,2,3,4,5]
#output: [1,3,6,10,15]

def toSum(nums):
    sum=0
    for i in range(0,len(nums)):
       sum=sum+nums[i]
       nums[i]=sum
    return nums

nums=[1,2,3,4,5]
print(f"The list is : {toSum(nums)}")
 