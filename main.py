#main.py 
#Main file for running the game

import pygame


# 1. Initialize pygame
pygame.init()

# 2. Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Pygame Window")

# 3. Clock (controls FPS)
clock = pygame.time.Clock()
FPS = 60

# 4. Game loop
running = True
while running:
    # --- Event handling ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Update game state ---
    # (logic goes here)

    # --- Drawing ---
    screen.fill((30, 30, 30))  # background color

    # (draw objects here)

    pygame.display.update()
    clock.tick(FPS)

# 5. Quit safely
pygame.quit()
