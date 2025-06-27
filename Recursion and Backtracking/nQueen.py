class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Initialize the board
        chess = [['.' for _ in range(n)] for _ in range(n)]
        result = []

        def isSafe(board, row, col, n):
            # Check vertical up
            for i in range(row):
                if board[i][col] == 'Q':
                    return False

            # Check upper-left diagonal
            i, j = row - 1, col - 1
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1

            # Check upper-right diagonal
            i, j = row - 1, col + 1
            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1

            return True

        def nQueen(board, row, n):
            if row == n:
                # Convert board rows to strings and append
                result.append([''.join(r) for r in board])
                return

            for j in range(n):
                if isSafe(board, row, j, n):
                    board[row][j] = 'Q'
                    nQueen(board, row + 1, n)
                    board[row][j] = '.'  # Backtrack

        nQueen(chess, 0, n)
        return result
