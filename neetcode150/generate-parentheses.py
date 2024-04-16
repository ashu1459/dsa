class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # if open < n
        # if close < open
        # if open == close == n
        stack = []
        res = []

        def backtracking(openN, closeN):
            if openN == closeN == n:
                res.append(''.join(stack))

            if openN < n:
                stack.append('(')
                backtracking(openN + 1, closeN)
                stack.pop()
            
            if closeN < openN:
                stack.append(')')
                backtracking(openN, closeN + 1)
                stack.pop()
        
        backtracking(0, 0)

        return res