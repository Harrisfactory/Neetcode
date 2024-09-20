class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        #clean string
        s = s.strip()

        s = s.split()

        return len(s[-1])
