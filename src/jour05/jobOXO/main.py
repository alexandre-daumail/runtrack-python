from typing import Tuple, Optional

import pygame

# Constants
WINDOW_SIZE = (600, 600)
GRID_DIM = 3
MARGIN = 20

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

# Initialize Pygame
pygame.init()

# Create the window
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set the window caption
pygame.display.set_caption("TicTacToe1337")

# Initialize the grid
grid = [['', '', ''],
        ['', '', ''],
        ['', '', '']]


# Functions
def draw_grid():
    cell_width = (screen.get_width() - 2 * MARGIN) / GRID_DIM
    cell_height = (screen.get_height() - 2 * MARGIN) / GRID_DIM

    for row in range(GRID_DIM):
        for col in range(GRID_DIM):
            x = MARGIN + col * cell_width
            y = MARGIN + row * cell_height
            rect = pygame.Rect(x, y, cell_width, cell_height)
            pygame.draw.rect(screen, GRAY, rect)

            if grid[row][col] == 'X':
                pygame.draw.line(screen, WHITE, rect.topleft, rect.bottomright, 10)
                pygame.draw.line(screen, WHITE, rect.bottomleft, rect.topright, 10)
            elif grid[row][col] == 'O':
                pygame.draw.circle(screen, WHITE, rect.center, int(cell_width / 2) - 10, 10)


def get_clicked_cell(pos: Tuple[int, int]) -> Optional[Tuple[int, int]]:
    x, y = pos
    for row in range(GRID_DIM):
        for col in range(GRID_DIM):
            rect = pygame.Rect(
                MARGIN + col * (screen.get_width() - 2 * MARGIN) / GRID_DIM,
                MARGIN + row * (screen.get_height() - 2 * MARGIN) / GRID_DIM,
                (screen.get_width() - 2 * MARGIN) / GRID_DIM - 2 * MARGIN,
                (screen.get_height() - 2 * MARGIN) / GRID_DIM - 2 * MARGIN,
            )
            if rect.collidepoint(x, y):
                return row, col
    return None


def check_winner():
    for row in range(GRID_DIM):
        if grid[row][0] == grid[row][1] == grid[row][2] is not None:
            return grid[row][0]
    for col in range(GRID_DIM):
        if grid[0][col] == grid[1][col] == grid[2][col] is not None:
            return grid[0][col]
    if grid[0][0] == grid[1][1] == grid[2][2] is not None:
        return grid[0][0]
    if grid[0][2] == grid[1][1] == grid[2][0] is not None:
        return grid[0][2]
    if all(all(cell is not None for cell in row) for row in grid):
        return 'Tie'
    return None


player = 'X'

draw_grid()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            cell = get_clicked_cell(event.pos)
            if cell is not None and grid[cell[0]][cell[1]] is None:
                grid[cell[0]][cell[1]] = player
                draw_grid()
                winner = check_winner()
                if winner is not None:
                    if winner == 'Tie':
                        message = "It's a tie!"
                    else:
                        message = "Player {} wins!".format(winner)
                    font = pygame.font.SysFont('Calibri', 48)
                    text = font.render(message, True, WHITE, BLACK)
                    text_rect = text.get_rect(center=screen.get_rect().center)
                    screen.fill(BLACK)
                    screen.blit(text, text_rect)
                    pygame.display.flip()
                    pygame.time.wait(3000)
                    running = False
                player = 'O' if player == 'X' else 'X'

    pygame.display.flip()

pygame.quit()
