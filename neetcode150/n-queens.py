class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:       
        res, combs = [], []
        
        queensPos = []
        for c in range(n):
            queensPos.append(0)

        def moveAllowed(queensPos, r, c):
            for col, row in enumerate(queensPos[:c]):
                dist = c - col
                if (
                    r == row 
                    or r >= n
                    or (r == row + dist and c == col + dist)
                    or (r == row - dist and c == col + dist)
                ):
                    return False
            return True

        def backtrack(allQueensPos, currQueenCol):
            if currQueenCol >= n:
                combs.append(allQueensPos.copy())
                return

            r = allQueensPos[currQueenCol]                

            for i in range(n):
                if moveAllowed(allQueensPos, r, currQueenCol):
                    prevR = allQueensPos[currQueenCol]
                    allQueensPos[currQueenCol] = r
                    backtrack(allQueensPos, currQueenCol + 1)
                    allQueensPos[currQueenCol] = prevR
                r += 1
            
            if r >= n:
                return

        backtrack(queensPos, 0)

        for comb in combs:
            board = []
            for row in comb:
                defaultStr = ['.' for i in range(n)]
                defaultStr[row] = 'Q'
                board.append(''.join(defaultStr))
            res.append(board)

        return res