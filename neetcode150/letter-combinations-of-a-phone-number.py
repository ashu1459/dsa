class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        res = []

        def dfs(prevChar, pos):
            if pos >= len(digits):
                res.append(prevChar)
                return

            for char in mapping[digits[pos]]:
                dfs(prevChar + char, pos + 1)
        dfs('', 0)
        return res
        