class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        

        #we want a window as a stack, as long as a repeat is found, continue popping left (removing from window), compare longest each time


        window = []
        longest_substring = 0

        for i in range(len(s)):
            while s[i] in window:
                window.pop(0)
            window.append(s[i])
            longest_substring = max(longest_substring, len(window))
        return longest_substring

        #O(n * k) where n is the length of s and k is the length of window anytime a repetive char is found
