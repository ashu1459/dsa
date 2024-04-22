class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        q = []
        zeros = {}
        untouchableZeros = set()
        ROWS, COLS = len(board), len(board[0])

        def visit(r, c):
            if (r < 0 or c < 0
                or r == ROWS or c == COLS
                or board[r][c] == 'X'
                or (r,c) in untouchableZeros):
                return

            q.append([r,c])
            del zeros[(r,c)]
            untouchableZeros.add((r,c))
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    if r == 0 or c == 0 or r == ROWS-1 or c == COLS-1:
                        untouchableZeros.add((r,c))
                        q.append([r,c])
                    else:
                        zeros[(r,c)] = 1

        while q:
            for i in range(len(q)):
                r, c = q.pop(0)
                visit(r + 1, c)
                visit(r - 1, c)
                visit(r, c + 1)
                visit(r, c - 1)

        for pos in zeros:
            r, c = pos
            board[r][c] = 'X'