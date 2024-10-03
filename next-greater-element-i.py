class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        results = []
        for i in range(len(nums1)):
            num2Index = nums2.index(nums1[i])
            nextGreater = -1
            for j in range(num2Index, len(nums2)):
                if nums2[j] > nums2[num2Index]:
                    nextGreater = nums2[j]
                    break
            results.append(nextGreater)
        
        return results
