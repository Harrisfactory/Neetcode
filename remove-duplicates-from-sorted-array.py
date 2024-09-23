class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        uniques = set()

        for i in reversed(range(len(nums))):
            if nums[i] in uniques:
                nums.pop(i)
            else:
                uniques.add(nums[i])
        
        return len(nums)
