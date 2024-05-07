class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROWS, COLS = len(matrix), len(matrix[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        
        output = []
        hashset = set()
        r, c, d = 0, 0, 0

        while True:
            hashset.add((r,c))
            output.append(matrix[r][c])

            # check if next row, col is out of bound
            nextR = r + directions[d][0]
            nextC = c + directions[d][1]
            
            if (nextR,nextC) in hashset or nextC < 0 or nextR == ROWS or nextC == COLS:
                if len(hashset) == (ROWS * COLS):
                    return output

                # switch to next direction (After last, move back to first direction)
                d = (d + 1) % 4

            r += directions[d][0]
            c += directions[d][1]