class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        elems = {}

        for num in nums:
            if num in elems:
                elems[num]+=1
            else:
                elems[num] = 1
        
        result = []

        while k > 0:
            max_key = None
            max_val = None
            for key, val in elems.items():
                if max_val and val > max_val:
                    max_val = val
                    max_key = key
                elif not max_val:
                    max_val = val
                    max_key = key
        
            result.append(max_key)
            del elems[max_key]
            k-=1

        return result
