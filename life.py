# life.py
import pygame
from utils import parse_args
from game import next_gen, random_fill, save_pattern, load_pattern

CELL_SIZE = 20
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

def main():
    args = parse_args()
    width, height = args.width, args.height
    screen_width, screen_height = width * CELL_SIZE, height * CELL_SIZE

    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Conway's Game of Life")

    running, paused = True, True
    live_cells = set()

    generation = 0

    while running:
        screen.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = not paused
                elif event.key == pygame.K_c:
                    live_cells.clear()
                elif event.key == pygame.K_r:
                    live_cells = random_fill(width, height)
                elif event.key == pygame.K_s:
                    save_pattern(live_cells)
                elif event.key == pygame.K_l:
                    live_cells = load_pattern()
                elif event.key == pygame.K_n and paused:
                    live_cells = next_gen(live_cells)
                    generation += 1

        # Update logic
        if not paused:
            live_cells = next_gen(live_cells)
            generation += 1

        # Draw grid
        for x, y in live_cells:
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, GREEN, rect)

        pygame.display.flip()
        clock.tick(args.fps)

    pygame.quit()

if __name__ == "__main__":
    main()
