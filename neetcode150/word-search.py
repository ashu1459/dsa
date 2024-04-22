class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(pos, r, c):
            if pos == len(word):
                return True
            if (r < 0 
                or c < 0
                or r >= len(board)
                or c >= len(board[0])
                or word[pos] != board[r][c] 
                ):
                return False
            # changing the value/char of visited box so that we dont cross it again
            board[r][c] = '.'
            res = (backtrack(pos + 1, r + 1, c)
                    or backtrack(pos + 1, r - 1, c)
                    or backtrack(pos + 1, r, c + 1)
                    or backtrack(pos + 1, r, c - 1))
            # assinging back the char value to board
            board[r][c] = word[pos]
            
            return res

        for r in range(len(board)):
            for c in range(len(board[0])):
                if backtrack(0, r, c):
                    return True
        
        return False