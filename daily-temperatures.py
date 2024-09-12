class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        result = [0] * len(temperatures)

        stack = [] #2d [value, index]

        for i in range(len(temperatures)):
            #while we have a stack and our current days temp is higher than the latest temp previous
            while len(stack) > 0 and temperatures[i] > stack[-1][0]:
                #set the result to the difference of days at that index
                result[stack[-1][1]] = i - stack[-1][1]
                #discard current day because weve found hotter
                stack.pop()
            #either at the end of stack comparison or without, add day
            stack.append([temperatures[i], i])
        
        return result
