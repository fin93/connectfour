board_cols = 7
board_rows = 6
player_o = "o"
player_x = "x"
board = [
    ["-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-"]
]


def print_board(boar):
    for i in range(board_rows):
        for j in range(board_cols):
            print(boar[i][j], end=" ")
        print()


def check_if_won(active):
    for i in range(board_rows):
        for j in range(board_cols - 3):
            if board[i][j] == board[i][j + 1] and board[i][j] == active:
                if board[i][j] == board[i][j + 2] and board[i][j] == board[i][j + 3]:
                    print(f"{active} Wins!")
                    quit()
    for z in range(board_rows - 3):
        for y in range(board_cols):
            if board[z][y] == board[z + 1][y] and board[z][y] == active:
                if board[z][y] == board[z + 2][y] and board[z][y] == board[z + 3][y]:
                    print(f"{active} Wins!")
                    quit()
    for k in range(board_rows - 3):
        for u in range(board_cols - 3):
            if board[k][u] == board[k + 1][u + 1] and board[k][u] == active:
                if board[k][u] == board[k + 2][u + 2] and board[k][u] == board[k + 3][u + 3]:
                    print(f"{active} Wins!")
                    quit()
    for d in range(3, board_rows):
        for lo in range(board_cols - 3):
            if board[d][lo] == board[d - 1][lo + 1] and board[d][lo] == active:
                if board[d][lo] == board[d - 2][lo + 2] and board[d][lo] == board[d - 3][lo + 3]:
                    print(f"{active} Wins!")
                    quit()


def is_free(col, active_player):
    for i in range(board_rows):
        if board[5][col] == "-":
            board[5][col] = active_player
            break

        elif board[i][col] != "-":
            board[i - 1][col] = active_player
            break


def main(active_player=1):
    while True:
        if active_player == 1:
            is_free(int(input("Enter the column: ")) - 1, player_o)
            print_board(board)
            check_if_won(player_o)
        elif active_player == -1:
            is_free(int(input("Enter the column: ")) - 1, player_x)
            print_board(board)
            check_if_won(player_x)
        active_player *= -1


if __name__ == '__main__':
    main()
