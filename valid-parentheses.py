class Solution:
    def isValid(self, s: str) -> bool:
        
        #create a dictionary to match open keys with closed as values

        #create a stack to place open keys on until a closed is found, then compare to match


        matcher = {
            '(':')',
            '{':'}',
            '[':']'
        }

        open_stack = []

        for i in range(len(s)):
            if s[i] in matcher:
                open_stack.append(s[i])
            else: #closed found, compare
                if len(open_stack) > 0 and matcher[open_stack.pop()] == s[i]:
                    continue
                return False
        
        if len(open_stack) > 0:
            return False
        return True

        #O(n) for number of paranth elements
