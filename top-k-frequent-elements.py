class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        freq_counter = {}

        for num in nums:
            if num in freq_counter:
                freq_counter[num]+=1
            else:
                freq_counter[num] = 1

        result = []
        while k > 0:
            max_key = None
            max_val = None

            for key, val in freq_counter.items():
                if max_key is None:
                    #set initial max
                    max_key = key
                    max_val = val
                elif max_val < val:
                    max_key = key
                    max_val = val
            del freq_counter[max_key]
            k-=1
            result.append(max_key)
        
        return result
