class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = {}

        for st in strs:
            sorted_str = str(sorted(st))
            if sorted_str in anagrams:
                anagrams[sorted_str].append(st)
            else:
                anagrams[sorted_str] = [st]
        
        return anagrams.values()
