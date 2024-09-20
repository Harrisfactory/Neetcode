class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        

        ctr = 0

        while ctr < len(s):
            for char in t:
                if s[ctr] == char:
                    ctr+=1
                    if ctr >= len(s):
                        return True
            return False
        
        if ctr >= len(s):
            return True
        return False
