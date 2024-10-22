class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        #pattern: I think sliding window because we are targeting a piece of one string in a 2nd larger string

        #plan:

            #capture len of s1, this is our window for s2

            #dont sort

            #if hit s1[0], we can then check both forward and backward for the permutation

            #if we reach the end false, else if we hit a perm at any time, true


        #capture len of s1
        s1Len = len(s1) - 1
        sortedS1 = sorted(s1)

        windowL, windowR = 0, s1Len + 1

        while windowL < len(s2):
            #target only if s1[0] is in s2
            if s1[0] in s2[windowL:windowR]:
                if sorted(s2[windowL:windowR]) == sortedS1:
                    return True
            windowL+=1
            windowR+=1

        return False
