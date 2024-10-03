class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        nums.sort()

        if nums[len(nums) // 2] == nums[0]:
            return nums[0]
        return nums[(len(nums) // 2) + 1]
