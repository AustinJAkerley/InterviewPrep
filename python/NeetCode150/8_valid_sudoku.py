class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0, 9):
            row = []
            column = []
            box = []
            for j in range(0, 9):
                if board[i][j] != '.':
                    if board[i][j] in row:
                        return False
                    row.append(board[i][j])

                if board[j][i] != '.':
                    if board[j][i] in column:
                        return False
                    column.append(board[j][i])

                box_row = 3 * (i // 3) + j // 3
                box_col = 3 * (i % 3) + j % 3
                if board[box_row][box_col] != '.':
                    if board[box_row][box_col] in box:
                        return False
                    box.append(board[box_row][box_col])

        return True