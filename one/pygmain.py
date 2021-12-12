import pygame

board_cols = 7
board_rows = 6
board = [
    ["-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-"]
]

WIDTH, HEIGHT = 700, 606
BG_COLOUR = 28, 170, 156
line_colour = 13, 141, 126
player_x_colour = 84, 84, 84
player_o_colour = 239, 231, 200
is_playing = True

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(BG_COLOUR)
font = pygame.font.SysFont('comicsans', 25)


def check_if_won(active):
    global is_playing
    for i in range(board_rows):
        for j in range(board_cols - 3):
            if board[i][j] == board[i][j + 1] and board[i][j] == active:
                if board[i][j] == board[i][j + 2] and board[i][j] == board[i][j + 3]:
                    is_playing = False
                    text = font.render(f"{active.upper()} Wins!", True, player_x_colour)
                    screen.blit(text, ((WIDTH // 2) - (text.get_width() // 2), 30))

    for z in range(board_rows - 3):
        for y in range(board_cols):
            if board[z][y] == board[z + 1][y] and board[z][y] == active:
                if board[z][y] == board[z + 2][y] and board[z][y] == board[z + 3][y]:
                    is_playing = False
                    text = font.render(f"{active.upper()} Wins!", True, player_x_colour)
                    screen.blit(text, ((WIDTH // 2) - (text.get_width() // 2), 30))

    for k in range(board_rows - 3):
        for u in range(board_cols - 3):
            if board[k][u] == board[k + 1][u + 1] and board[k][u] == active:
                if board[k][u] == board[k + 2][u + 2] and board[k][u] == board[k + 3][u + 3]:
                    is_playing = False
                    text = font.render(f"{active.upper()} Wins!", True, player_x_colour)
                    screen.blit(text, ((WIDTH // 2) - (text.get_width() // 2), 30))

    for d in range(3, board_rows):
        for lo in range(board_cols - 3):
            if board[d][lo] == board[d - 1][lo + 1] and board[d][lo] == active:
                if board[d][lo] == board[d - 2][lo + 2] and board[d][lo] == board[d - 3][lo + 3]:
                    is_playing = False
                    text = font.render(f"{active.upper()} Wins!", True, player_x_colour)
                    screen.blit(text, ((WIDTH // 2) - (text.get_width() // 2), 30))


def is_free(col, a_p):
    for i in range(board_rows):
        if board[5][col] == "-":
            board[5][col] = a_p
            break

        elif board[i][col] != "-":
            board[i - 1][col] = a_p
            break


def print_board():
    for i in range(board_rows):
        for j in range(board_cols):
            if board[i][j] != "-" and board[i][j] == "x":
                row = j + 1
                col = i + 1
                pygame.draw.circle(screen, player_x_colour, (((row * 100) - 50), (col * 100) - 50), 30)

            if board[i][j] != "-" and board[i][j] == "o":
                row = j + 1
                col = i + 1
                pygame.draw.circle(screen, player_o_colour, (((row * 100) - 50), (col * 100) - 50), 30)


def draw_lines():
    pygame.draw.line(screen, line_colour, (2, 0), (5, 600), 10)
    pygame.draw.line(screen, line_colour, (695, 0), (695, 600), 10)
    for i in range(1, 7):
        j = i * 100
        pygame.draw.line(screen, line_colour, (0, j), (WIDTH, j), 10)
        pygame.draw.line(screen, line_colour, (j, 10), (j, 600), 10)


def restart():
    global is_playing
    for i in range(board_rows):
        for j in range(board_cols):
            board[i][j] = "-"
    screen.fill(BG_COLOUR)
    draw_lines()
    is_playing = True


draw_lines()
active_player = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN and is_playing:
            mouse_x = event.pos[0]

            clicked_col = (mouse_x // 100)
            if active_player == 1:
                is_free(clicked_col, "o")
                print_board()
                
                check_if_won("o")
            elif active_player == -1:
                is_free(clicked_col, "x")
                print_board()
                check_if_won("x")
            active_player *= -1

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
            if event.key == pygame.K_r:
                restart()

    pygame.display.update()
