class Solution:
    def isValid(self, s: str) -> bool:
        close_open = {
            '}' : '{',
            ')' : '(',
            ']' : '['
        }

        stack = []

        for c in s:
            if c in close_open:
                # if len(stack) == 0 or close_open[c] != stack.pop():
                #     return False
                if stack and close_open[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        # return len(stack) == 0
        return not stack

        