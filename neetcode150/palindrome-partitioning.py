class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []
        
        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return
            for j in range(i, len(s)):
                string = s[i:j+1]
                if string == string[::-1]:
                    part.append(string)
                    dfs(j + 1)
                    part.pop()
        dfs(0)
        return res