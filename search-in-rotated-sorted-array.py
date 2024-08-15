class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            
            #now check which portion of the array were in
            #are we in the left sorted portion?
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]: #the or accounts for the pivot point
                    #we'll need to search right
                    l = mid + 1
                else: #the target is less than the middle or greater than the left pointer so we search left
                    r = mid - 1
            else:#we are in the right sorted portion
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
            
        return -1
