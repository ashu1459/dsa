class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        pacific, atlantic = set(), set()
        ROWS, COLS = len(heights), len(heights[0])

        def dfs(r, c, visited, prevHeight):
            if (r < 0 or c < 0
                or r == ROWS or c == COLS
                or (r, c) in visited
                or heights[r][c] < prevHeight
                ):
                return
            
            visited.add((r,c))
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])
 
        for c in range(COLS):
            # get heights that can reach pacific ocean
            dfs(0, c, pacific, heights[0][c])
            # get heights that can reach atlantic ocean
            dfs(ROWS - 1, c, atlantic, heights[ROWS - 1][c])

        for r in range(ROWS):
            # get heights that can reach pacific ocean
            dfs(r, 0, pacific, heights[r][0])
            # get heights that can reach atlantic ocean
            dfs(r, COLS - 1, atlantic, heights[r][COLS - 1])
        
        # get heights that can reach pacific and atlantic both
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])

        return res

                