def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows, columns, and diagonals
    return any(
        all(cell == player for cell in line)
        for line in (board + list(map(list, zip(*board))) + [[board[i][i] for i in range(3)], [board[i][2 - i for i in range(3)]]])
    )

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    while True:
        print_board(board)
        row = int(input(f"Player {players[turn % 2]}, enter the row (0, 1, or 2): "))
        col = int(input(f"Player {players[turn % 2]}, enter the column (0, 1, or 2): "))

        if board[row][col] == " ":
            board[row][col] = players[turn % 2]
            if check_winner(board, players[turn % 2]):
                print_board(board)
                print(f"Player {players[turn % 2]} wins!")
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break
            turn += 1
        else:
            print("Cell already taken, please choose another.")

if __name__ == "__main__":
    main()
