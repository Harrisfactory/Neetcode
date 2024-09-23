class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        record = []

        for i in range(len(operations)):
            #insert x onto stack
            if operations[i] == '+':
                record.append(int(record[-1]) + int(record[-2]))
            elif operations[i] == 'D': #we just peek onto the stack and double it
                record.append(int(record[-1]) * 2)
            elif operations[i] == 'C': # we just pop from the stack
                record.pop()
            else:
                record.append(int(operations[i]))
        return sum(record)
