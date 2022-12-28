class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        i = 0
        y = 0
        x = len(nums)
        for i in range (len(nums)):
            if nums.count(nums[i])>x/2:
                y = (nums[i])
                break
        return(y)
            
