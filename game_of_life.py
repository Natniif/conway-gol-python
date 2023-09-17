import pygame
import time
import random

WIDTH, HEIGHT = 800, 800
GRID_SIZE = 100
CELL_SIZE = WIDTH // GRID_SIZE
FPS = 5

BLACK = (0, 0, 0)
GREEN = (57, 255, 20)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Conways game of life")

grid = [[random.choice([0, 1]) for _ in range(GRID_SIZE)]
        for _ in range(GRID_SIZE)]


def update_grid() -> None:
    global grid
    updated_grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            conway(updated_grid, i, j)

    grid = updated_grid


def conway(updated_grid: list, i: int, j: int):

    neighbours = []

    for x in range(i-1, i+2):
        for y in range(j-1, j+2):
            if 0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE and (x != i or y != j):
                neighbours.append(grid[x][y])

    alive = sum(neighbours)

    if (grid[i][j] == 0):
        if (alive == 3):
            # becomes alive
            updated_grid[i][j] = 1
        else:
            updated_grid[i][j] = 0
    elif (grid[i][j] == 1):
        if (alive < 2 or alive > 3):
            updated_grid[i][j] = 0
        elif (alive == 2 or alive == 3):
            updated_grid[i][j] = 1


def draw_grid() -> None:
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            color = GREEN if grid[i][j] else BLACK
            rect = pygame.Rect(j * CELL_SIZE, i * CELL_SIZE,
                               CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, color, rect)


def main() -> None:
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_grid()
        update_grid()

        pygame.display.flip()

        clock.tick(FPS)
        time.sleep(0.1)

    pygame.quit()


if __name__ == "__main__":
    main()
