class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        ROWS, COLS = len(grid), len(grid[0])

        def backtrack(r, c):
            if (r < 0 or c < 0
                or r == ROWS or c == COLS
                or grid[r][c] == 0):
                return 0
            
            # mark position as visited
            grid[r][c] = 0
            # count land from every direction and add 1 for current land
            return (1 
                    + backtrack(r + 1, c)
                    + backtrack(r - 1, c)
                    + backtrack(r, c + 1)
                    + backtrack(r, c - 1))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    landCount = backtrack(r, c)
                    res = max(res, landCount)

        return res