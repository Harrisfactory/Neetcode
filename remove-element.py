class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        ctr = len(nums) - 1

        while ctr >= 0:
            if nums[ctr] == val:
                nums.pop(ctr)
            ctr-=1
        return len(nums)
