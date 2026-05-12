
N = int(input("Enter the number of queens: "))
board = [[0] * N for _ in range(N)]

def is_attack(row, col):
    for i in range(N):
        if board[row][i] == 1 or board[i][col] == 1:
            return True
    for i in range(N):
        for j in range(N):
            if abs(row - i) == abs(col - j) and board[i][j] == 1:
                return True
    return False

def solve_n_queens(n):
    if n == 0:
        return True
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0 and not is_attack(i, j):
                board[i][j] = 1
                if solve_n_queens(n - 1):
                    return True
                board[i][j] = 0
    return False

if solve_n_queens(N):
    print("Solution for the N-Queens Problem:")
    for row in board:
        print(row)
else:
    print("No solution exists.")
