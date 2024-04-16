class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        if len(tokens) == 1:
            return int(tokens[0])

        stack = []
        # valid_operations = set(['+', '-', '*', '/'])
        # calculation = 0

        # for token in tokens:
        #     if token in valid_operations:
        #         second = stack.pop()
        #         first = stack.pop()
                
        #         if token == '+':
        #             calculation = float(first) + float(second)
        #         elif token == '-':
        #             calculation = float(first) - float(second)
        #         elif token == '/':
        #             calculation = int(float(first) / float(second))
        #         elif token == '*':
        #             calculation = float(first) * float(second)

        #         stack.append(calculation)
        #     else:
        #         stack.append(token)

        # return int(calculation) if int(calculation) == calculation else calculation

        for c in tokens:
            if c == '+':
                stack.append(stack.pop() + stack.pop())
            elif c == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            elif c == '*':
                stack.append(stack.pop() * stack.pop())
            else:
                stack.append(int(c))

        return stack[0]
