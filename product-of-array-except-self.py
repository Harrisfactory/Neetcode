import numpy

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        seen_nums = {}
        result = []

        for i in range(len(nums)):
            if nums[i] in seen_nums:
                result.append(seen_nums[nums[i]])
                continue
            left_product = numpy.prod(nums[0:i])
            right_product = numpy.prod(nums[i+1:])
            seen_nums[nums[i]] = int(left_product * right_product)
            result.append(int(left_product * right_product))
        
        return result
