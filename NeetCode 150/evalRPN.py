class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        evalStack = []
        for token in tokens:
            try:
                evalStack.append(int(token))
            except ValueError:
                operand = evalStack.pop()
                current = evalStack.pop()
                print(current)
                print(operand)
                print(token)

                match token:
                    case "+":
                        current = current + operand
                    case "-":
                        current = current - operand
                    case "*":
                        current = current * operand
                    case "/":
                        current = int(current / operand)
                    
                evalStack.append(current)
        
        return evalStack[-1]≈
