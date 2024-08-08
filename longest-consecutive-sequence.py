class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #convert nums to set 
        #if left of cur num is not in set
            #inc length of cur sequence until right neighbor not in set
        #then update longest

        #converting nums to a set of nums so that we avoid repeats
        numSet = set(nums)
        max_length = 0

        for num in nums:
            #this detects if we are at the start of a new sequence
            if num - 1 not in numSet:
                #we want to reset our current_length every time we restart a sequence
                cur_len = 1
                while num + cur_len in numSet: #here we are detecting if next neighbor exists
                    cur_len+=1
                #we want to compare our current length with our current max length
                max_length = max(max_length, cur_len)
        
        return cur_len
