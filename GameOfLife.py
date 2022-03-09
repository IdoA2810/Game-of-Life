import pygame
import random

MAX_FPS = 10


HEIGHT = 600
WIDTH = 600
ROWS = 20
COLS = 20

SQ_SIZE = HEIGHT  // ROWS
'''
Rules:

1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
2. Any live cell with two or three live neighbours lives on to the next generation.
3. Any live cell with more than three live neighbours dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
'''

def generate_board(rows, cols):
        board = []
        for i in range(rows):
            new = []
            for j in range(cols):
                new.append(random.randint(0,1))
            board.append(new)

        return board

def draw_board(screen, board, rows, cols):
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 1:
                pygame.draw.rect(screen, pygame.Color("WHITE"), pygame.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
                pygame.draw.rect(screen, pygame.Color("BLACK"), pygame.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE),1)
            else:
                pygame.draw.rect(screen, pygame.Color("BLACK"), pygame.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))

def count_neighbors(board, row, col):
    sum = 0
    for i in range(-1, 2):
        x = row + i
        if x < 0:
            x = ROWS - 1
        elif x == ROWS:
            x = 0
        for j in range(-1, 2):
            y = col + j
            if y < 0:
                y = COLS - 1
            elif y == COLS:
                y = 0
            sum += board[x][y]
    sum -= board[row][col]
    return sum




def new_generation(board, rows, cols):
    new_board = []
    for i in range(rows):
        new = []
        for j in range(cols):
            #count live neighbors
            sum = count_neighbors(board, i, j)

            if 2 <= sum <= 3 and board[i][j] == 1: #Rule number 2
                new.append(1)
            elif sum == 3 and board[i][j] == 0: #Rule number 4
                new.append(1)
            else: # Rules 1 and 3
                new.append(0)
        new_board.append(new)
    return new_board




def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    running = True

    board = generate_board(ROWS, COLS)
    draw_board(screen, board, ROWS, COLS)

    clock.tick(MAX_FPS)
    pygame.display.flip()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        board = new_generation(board, ROWS, COLS)
        draw_board(screen, board, ROWS, COLS)


        clock.tick(MAX_FPS)
        pygame.display.flip()

if __name__ == "__main__":
    main()
