class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        operandStack = []

        operators = ['+','-','*','/']

        for i in range(len(tokens)):
            if tokens[i] in operators and len(operandStack) > 1:
                operandL = int(operandStack.pop())
                operandR = int(operandStack.pop())
                if tokens[i] == '+':
                    operandStack.append(operandL + operandR)
                elif tokens[i] == '-':
                    operandStack.append(operandR - operandL)
                elif tokens[i] == '*':
                    operandStack.append(operandL * operandR)
                else:
                    operandStack.append(operandR / operandL)
            else:
                operandStack.append(tokens[i])
        
        return int(operandStack[0])
