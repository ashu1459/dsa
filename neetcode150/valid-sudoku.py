class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        box_row_start = 0
        seen = [[], [], [], [], [], [], [], [], []]
        seen_row = [[], [], [], [], [], [], [], [], []]
        seen_column = [[], [], [], [], [], [], [], [], []]

        # for r in range(len(board)):
        #     box_row = box_row_start

        #     for c, num in enumerate(board[r]):
        #         if num == '.':
        #             continue
        #         if (
        #                 num in seen[box_row] or
        #                 num in seen_column[c] or
        #                 num in seen_row[r]
        #             ):
        #             return False

        #         seen[box_row].append(num)
        #         seen_row[r].append(num)
        #         seen_column[c].append(num)

        #         if c % 3 == 2:
        #             box_row += 1

        #     if r % 3 == 2:
        #         box_row_start = r + 1

        seen = [
            [[], [], []], [[], [], []], [[], [], []]
        ]

        for r in range(len(board)):
            for c, num in enumerate(board[r]):
                if num == '.':
                    continue

                if (
                        num in seen[r//3][c//3] or
                        num in seen_column[c] or
                        num in seen_row[r]
                    ):
                    return False

                seen_row[r].append(num)
                seen_column[c].append(num)
                seen[r//3][c//3].append(num)

        return True
