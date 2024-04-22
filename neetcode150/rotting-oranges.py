class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = []
        freshCount = 0
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])

        def rot(r, c, freshCount):
            if (r < 0 or c < 0
                or r == ROWS or c == COLS
                or grid[r][c] == 2
                or grid[r][c] == 0
                or (r,c) in visited
                ):
                return freshCount
            visited.add((r,c))
            q.append([r,c])

            return freshCount - 1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r,c])
                    visited.add((r,c))
                elif grid[r][c] == 1:
                    freshCount += 1

        time = 0
        while q and freshCount:
            for i in range(len(q)):
                r, c = q.pop(0)
                grid[r][c] = 2
                freshCount = rot(r + 1, c, freshCount)
                freshCount = rot(r - 1, c, freshCount)
                freshCount = rot(r, c + 1, freshCount)
                freshCount = rot(r, c - 1, freshCount)
            time += 1
        
        return -1 if freshCount else time