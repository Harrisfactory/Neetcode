class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        #two pointer since we want a large container

        #we can only get the smallest of the two heights as to not spill

        #calculate area and compare against current max area, this is your answer

        l, r = 0, len(height) - 1

        max_water = 0

        while l < r:
            cur_water = min(height[l], height[r]) * (r-l)
            max_water = max(max_water, cur_water)
            if height[l] < height[r]:
                l+=1
            elif height[r] < height[l]:
                r-=1
            else:
                l+=1
                r-=1
        return max_water 

        #O(nlog(n))   
