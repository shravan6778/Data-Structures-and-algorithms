def toSum(nums):
    sum=0
    for i in range(0,len(nums)):
       sum=sum+nums[i]
    return sum

nums=[1,2,3,4,5]
print(f"The sum of the list is : {toSum(nums)}")
 