class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        grid = [[0 for i in range(len(text1) + 1)] for j in range(len(text2) + 1)]
        
        for r in range(len(text2) - 1, -1, -1):
            for c in range(len(text1) - 1, -1, -1):
                if text2[r] == text1[c]:
                    grid[r][c] = 1 + grid[r + 1][c + 1]
                else:
                    grid[r][c] = max(grid[r + 1][c], grid[r][c + 1])
        
        return grid[0][0]