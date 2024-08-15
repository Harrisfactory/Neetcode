class Solution:
    def findMin(self, nums: List[int]) -> int:
        

        #we want to find the minimum, using binary search 
        
        #if our middle is larger than our left pointer then we want to search left BECAUSE that means we are on the larger half of pivot

        #otherwise we are on the smaller half of pivot

        #we can tell if were at minimum if right pointer is > than left pointer, update running result as left


        result = 5001

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            #compare running result
            result = min(nums[mid], result)

            if nums[l] <= nums[r]: #we are within a sorted window, compare minimum with running result
                result = min(nums[l], result)
            if nums[mid] >= nums[l]: #we are on the large side, so we should search right
                l = mid + 1
            elif nums[mid] <= nums[r]: #we are on the small side, search left
                r = mid - 1

        return result
            
        #O(log n)
