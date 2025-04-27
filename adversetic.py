import math

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[1][1]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[1][1]

    return None

def minimax(board, depth, maximizing):
    winner = check_winner(board)
    if winner == "X":
        return -1
    if winner == "O":
        return 1
    if all(board[row][col] != " " for row in range(3) for col in range(3)):
        return 0

    if maximizing:
        best = -math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = "O"
                    best = max(best, minimax(board, depth + 1, False))
                    board[row][col] = " "
        return best
    else:
        best = math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = "X"
                    best = min(best, minimax(board, depth + 1, True))
                    board[row][col] = " "
        return best

def best_move(board):
    move = None
    best_score = -math.inf

    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                board[row][col] = "O"
                score = minimax(board, 0, False)
                board[row][col] = " "

                if score > best_score:
                    best_score = score
                    move = (row, col)

    return move

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]

    print("Welcome to Tic-Tac-Toe!")
    print("You are 'X' and AI is 'O'.")
    print("Enter your move as row and column numbers (0, 1, or 2).")

    while True:
        print_board(board)

        try:
            row, col = map(int, input("Enter row and column (0-2) for X: ").split())
        except ValueError:
            print("Invalid input! Please enter two numbers between 0 and 2.")
            continue

        if not (0 <= row <= 2 and 0 <= col <= 2):
            print("Invalid move! Row and column must be between 0 and 2.")
            continue

        if board[row][col] != " ":
            print("Invalid move! Cell already occupied. Try again.")
            continue

        board[row][col] = "X"

        if check_winner(board):
            print_board(board)
            print("X wins!")
            break

        if all(board[row][col] != " " for row in range(3) for col in range(3)):
            print_board(board)
            print("It's a draw!")
            break

        ai_move = best_move(board)
        if ai_move:
            board[ai_move[0]][ai_move[1]] = "O"
            print(f"AI plays at: {ai_move[0]}, {ai_move[1]}")

            if check_winner(board):
                print_board(board)
                print("O wins!")
                break

        if all(board[row][col] != " " for row in range(3) for col in range(3)):
            print_board(board)
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
