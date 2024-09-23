class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        #going to traverse through s, if there is no match for t in dict or t ends, it fails

        wordMap = {}

        for i in range(len(s)):
            #if s exists in wordmap
            if s[i] in wordMap:
                #does t match up
                if i > len(t) or wordMap[s[i]] != t[i]:
                    return False
            else:
                #add s cur to wordMap
                if i > len(t):
                    return False
                #first check if t[i] is mapped already
                if t[i] in wordMap.values():
                    return False
                wordMap[s[i]] = t[i]
        return True
