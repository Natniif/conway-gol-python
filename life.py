import pygame
import random
import time
import argparse

WIDTH, HEIGHT = 800, 800
BLACK = (0, 0, 0)
GREEN = (57, 255, 20)


def initialise_grid(size: int):
    return [[random.choice([0, 1]) for _ in range(size)]
            for _ in range(size)]


def update_grid(grid):
    updated_grid = [[0 for _ in range(len(grid))] for _ in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid)):
            conway(grid, updated_grid, i, j)

    return updated_grid


def conway(grid, updated_grid, i, j):
    neighbours = []

    for x in range(i-1, i+2):
        for y in range(j-1, j+2):
            if 0 <= x < len(grid) and 0 <= y < len(grid) and (x != i or y != j):
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


def draw_grid(grid_size, cell_size, grid, screen) -> None:
    for i in range(grid_size):
        for j in range(grid_size):
            color = GREEN if grid[i][j] else BLACK
            rect = pygame.Rect(j * cell_size, i * cell_size,
                               cell_size, cell_size)
            pygame.draw.rect(screen, color, rect)


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('--grid_size', type=int, default=100,
                        help="Number of cells on each axis")
    parser.add_argument('--fps', type=int, default=10,
                        help="Number of frames per second")

    args = parser.parse_args()
    FPS = args.fps
    GRID_SIZE = args.grid_size
    CELL_SIZE = WIDTH // GRID_SIZE

    grid = initialise_grid(GRID_SIZE)

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Conways game of life")

    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_grid(GRID_SIZE, CELL_SIZE, grid, screen)
        grid = update_grid(grid)

        pygame.display.flip()

        clock.tick(FPS)
        time.sleep(0.05)

    pygame.quit()


if __name__ == '__main__':
    main()
