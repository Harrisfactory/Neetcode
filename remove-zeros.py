class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        ctr = len(nums)-1

        while ctr >= 0:
            if nums[ctr] == 0:
                nums.append(nums[ctr])
                nums.pop(ctr)
            ctr-=1
