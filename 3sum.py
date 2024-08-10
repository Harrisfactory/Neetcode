class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        triplets = set()

        nums = sorted(nums)

        for i in range(len(nums)):
            l, r = i+1, len(nums) - 1
            while l < r:
                sum_num = nums[i] + nums[l] + nums[r]
                if nums[i] + nums[l] + nums[r] == 0:
                    triplets.add((nums[i], nums[l], nums[r]))
                    l+=1
                    r-=1
                    continue
                if sum_num > 0:
                    r-=1
                    continue
                if sum_num < 0:
                    l+=1
                    continue
        return triplets
