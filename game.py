# game.py
from random import randint

def next_gen(live_cells):
    neighbor_count = {}
    for x, y in live_cells:
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                neighbor = (x + dx, y + dy)
                neighbor_count[neighbor] = neighbor_count.get(neighbor, 0) + 1

    new_live = set()
    for cell, count in neighbor_count.items():
        if count == 3 or (count == 2 and cell in live_cells):
            new_live.add(cell)

    return new_live

def random_fill(width, height, density=0.2):
    return {
        (x, y)
        for x in range(width)
        for y in range(height)
        if randint(0, 100) < density * 100
    }

def save_pattern(live_cells, filename='patterns.txt'):
    with open(filename, 'w') as f:
        for x, y in sorted(live_cells):
            f.write(f"{x},{y}\n")

def load_pattern(filename='patterns.txt'):
    live_cells = set()
    with open(filename, 'r') as f:
        for line in f:
            if line.startswith('#') or not line.strip():
                continue
            x, y = map(int, line.strip().split(','))
            live_cells.add((x, y))
    return live_cells
