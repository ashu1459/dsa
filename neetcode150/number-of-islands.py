class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        ROWS, COLS = len(grid), len(grid[0])

        def backtrack(r, c):
            if (r < 0 or c < 0
                or r == ROWS or c == COLS
                or grid[r][c] == '0'):
                return

            # mark this position as visited/0
            grid[r][c] = '0'
            backtrack(r + 1, c)
            backtrack(r - 1, c)
            backtrack(r, c + 1)
            backtrack(r, c - 1)

        # visit valid land positions and is neighbours
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    backtrack(r, c)
                    res += 1
        
        return res