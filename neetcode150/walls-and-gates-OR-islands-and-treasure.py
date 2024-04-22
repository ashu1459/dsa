class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        doors = {}
        ROWS, COLS = len(grid), len(grid[0])

        # Solution-1: Recursive
        # def backtrack(r, c, step):
        #     if (
        #         r < 0 or c < 0
        #         or r == ROWS
        #         or c == COLS
        #         or grid[r][c] == -1
        #         or (step > 0 and step >= grid[r][c])
        #         ):
        #         return
            
        #     grid[r][c] = step
        #     backtrack(r + 1, c, step + 1)
        #     backtrack(r - 1, c, step + 1)
        #     backtrack(r, c + 1, step + 1)
        #     backtrack(r, c - 1, step + 1)
        
        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if grid[r][c] == 0:
        #             doors[(r,c)] = 1

        # for door in doors:
        #     r, c = door
        #     backtrack(r, c, 0)

        # return grid

        # Solution-2: O(mxn) Linear time (cisiting every node once only)
        visited = set()
        q = []
        def addStep(r, c):
            if (r < 0 or c < 0
                or r == ROWS or c == COLS
                or grid[r][c] == -1
                or (r,c) in visited):
                return
            q.append([r, c])
            visited.add((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visited.add((r,c))

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.pop(0)
                grid[r][c] = dist
                addStep(r + 1, c)
                addStep(r - 1, c)
                addStep(r, c + 1)
                addStep(r, c - 1)
            dist += 1
        
        return grid




