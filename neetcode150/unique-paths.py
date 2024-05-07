class Solution:
    ans = 0
    def uniquePaths(self, m: int, n: int) -> int:
        # Solution-1: Backtracking Approach
        # def dfs(r, c):
        #     if r >= m or c >= n:
        #         return
        #     if r == m-1 and c == n-1:
        #         self.ans += 1
            
        #     dfs(r + 1, c)
        #     dfs(r, c + 1)

        # dfs(0, 0)
        # return self.ans

        # Solution-2: DP approach: TC - O(m * n), SC: O(m * n)
        # grid = [[0 for i in range(n)] for j in range(m)]

        # # preparing the grid
        # for i in range(m):
        #     grid[i][n - 1] = 1
        # for j in range(n):
        #     grid[m - 1][j] = 1
        
        # for r in range(m - 2, -1, -1):
        #     for c in range(n - 2, -1, -1):
        #         grid[r][c] = grid[r + 1][c] + grid[r][c + 1]

        # return grid[0][0]

        # Solution-3: DP approach: TC - O(m * n), SC: O(n)
        row = [1] * n

        for i in range(m - 2, -1, -1):
            newRow = [1] * n
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow
        return row[0]