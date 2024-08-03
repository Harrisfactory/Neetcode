class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        num_hist = {}

        for i in range(len(nums)):
            if target - nums[i] in num_hist:
                return [i, num_hist[target - nums[i]]]
            num_hist[nums[i]] = i
