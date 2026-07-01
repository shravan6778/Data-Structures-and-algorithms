'''Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.'''

def sortArrayByParity(nums: List[int]) -> List[int]:
    start=0
    for i in range(0,len(nums)):
        if nums[i]%2==0:
            nums[start],nums[i]=nums[i],nums[start]
            start+=1
    return nums