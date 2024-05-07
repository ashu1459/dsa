class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set()
        minHeap = [[grid[0][0], 0, 0]]
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def isValidNei(r, c, visited):
            if (
                r < 0 or c < 0
                or r == n or c == n
                or grid[r][c] in visited
                ):
                return False
            
            return True

        visited.add(grid[0][0])
        while minHeap:
            maxElev, r, c = heapq.heappop(minHeap)

            if r == n - 1 and c == n - 1:
                return maxElev

            for neiR, neiC in directions:
                if isValidNei(r + neiR, c + neiC, visited):
                    curElev = grid[r + neiR][c + neiC]
                    visited.add(curElev)
                    heapq.heappush(minHeap, [max(maxElev, curElev), r + neiR, c + neiC])
                