class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        

        ctr = 0

        badFind = False

        lcp = ''

        while not badFind:
            #traverse first word for char to compare with all strs
            if len(strs[0]) <= 0 or len(strs[0]) <= ctr or strs == [""] or ctr > len(strs[0]):
                return lcp
            curChar = strs[0][ctr]
            #loop through each str and check only current ctr location, check for len breaking as well
            for i in range(len(strs)):
                if ctr < len(strs[i]) and strs[i][ctr] == curChar:
                    continue
                else:
                    return lcp
            lcp += strs[0][ctr]
            ctr+=1

        return lcp
