def print_board(board):
    """Helper function to print the board in a readable format."""
    for row in board:
        print(' '.join(str(x) for x in row))
    print("\n")

def is_safe(board, row, col, n):
    """Check if it's safe to place a queen at board[row][col]."""
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, col, n):
    """Solve the N-Queens problem using backtracking."""
    # Base case: If all queens are placed, return True
    if col >= n:
        return True

    # Consider this column and try placing this queen in all rows one by one
    for i in range(n):
        if is_safe(board, i, col, n):
            # Place this queen in board[i][col]
            board[i][col] = 1

            # Recur to place rest of the queens
            if solve_n_queens(board, col + 1, n):
                return True

            # If placing queen in board[i][col] doesn't lead to a solution,
            # then remove queen (backtrack)
            board[i][col] = 0

    # If the queen cannot be placed in any row in this column col, then return False
    return False

def n_queens(n):
    """Main function to solve the N-Queens problem for an NxN board."""
    # Create an NxN board initialized with 0
    board = [[0 for _ in range(n)] for _ in range(n)]

    if not solve_n_queens(board, 0, n):
        print("Solution does not exist")
        return False

    print_board(board)
    return True

# Ask the user for the size of the board (n)
n = int(input("Enter the number of queens: "))
n_queens(n)
