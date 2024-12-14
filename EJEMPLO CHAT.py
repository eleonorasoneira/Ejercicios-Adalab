import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 3
CELL_SIZE = WIDTH // GRID_SIZE
LINE_COLOR = (0, 0, 0)
WHITE = (255, 255, 255)

# Load images
PLAYER_IMAGE = pygame.image.load("player_x.png")  # Replace with your X image
PLAYER_IMAGE = pygame.transform.scale(PLAYER_IMAGE, (CELL_SIZE, CELL_SIZE))
COMPUTER_IMAGE = pygame.image.load("computer_o.png")  # Replace with your O image
COMPUTER_IMAGE = pygame.transform.scale(COMPUTER_IMAGE, (CELL_SIZE, CELL_SIZE))

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Game board
board = [[None for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

# Functions
def draw_grid():
    for x in range(1, GRID_SIZE):
        pygame.draw.line(screen, LINE_COLOR, (x * CELL_SIZE, 0), (x * CELL_SIZE, HEIGHT), 3)
        pygame.draw.line(screen, LINE_COLOR, (0, x * CELL_SIZE), (WIDTH, x * CELL_SIZE), 3)

def draw_board():
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if board[row][col] == "X":
                screen.blit(PLAYER_IMAGE, (col * CELL_SIZE, row * CELL_SIZE))
            elif board[row][col] == "O":
                screen.blit(COMPUTER_IMAGE, (col * CELL_SIZE, row * CELL_SIZE))

def check_winner():
    # Check rows, columns, and diagonals
    for row in range(GRID_SIZE):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] is not None:
            return board[row][0]

    for col in range(GRID_SIZE):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]

    return None

def is_full():
    return all(all(cell is not None for cell in row) for row in board)

def computer_move():
    empty_cells = [(row, col) for row in range(GRID_SIZE) for col in range(GRID_SIZE) if board[row][col] is None]
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = "O"

# Game loop
running = True
player_turn = True
winner = None

while running:
    screen.fill(WHITE)
    draw_grid()
    draw_board()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and player_turn and winner is None:
            x, y = event.pos
            row, col = y // CELL_SIZE, x // CELL_SIZE
            if board[row][col] is None:
                board[row][col] = "X"
                player_turn = False

    if not player_turn and winner is None:
        computer_move()
        player_turn = True

    winner = check_winner()
    if winner or is_full():
        if winner:
            print(f"{winner} wins!")
        else:
            print("It's a tie!")
        running = False

    pygame.display.flip()

pygame.quit()

