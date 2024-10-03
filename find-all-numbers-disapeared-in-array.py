class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        numLen = len(nums)
        #removing duplicates
        nums = set(nums)
        ctr = 1
        results = []
        while ctr <= numLen:
            while ctr not in nums and ctr <= numLen:
                results.append(ctr)
                ctr+=1
            ctr+=1
        return results
