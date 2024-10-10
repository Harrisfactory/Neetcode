class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        ctr1, ctr2 = 0, 0

        result = ''

        while ctr1 < len(word1) or ctr2 < len(word2):
            if ctr1 < len(word1):
                result+=word1[ctr1]
                ctr1+=1
            if ctr2 < len(word2):
                result+=word2[ctr2]
                ctr2+=1
        return result
