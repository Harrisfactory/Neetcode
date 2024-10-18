class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        nums.sort()
        ctr = 0

        while ctr < len(nums):
            if nums[ctr] != ctr:
                return ctr
            else:
                ctr+=1
                
        return ctr
