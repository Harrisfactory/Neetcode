class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        result = list(arr)

        ctr = len(arr) - 2

        cur_max = 0

        while ctr >= 0:
            cur_max = max(cur_max, arr[ctr + 1])
            result[ctr] = cur_max
            ctr-=1
        
        result[len(arr)-1] = -1
        return result
