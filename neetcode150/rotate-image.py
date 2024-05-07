class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        # TRANSPOSE the matrix
        for r in range(ROWS):
            for c in range(r, COLS):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
                
        # REVERSE the matrix
        for r in range(ROWS):
            matrix[r] = matrix[r][::-1]
        