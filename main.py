import pygame
from constants import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True
    while (running):
        for event in pygame.event.get():
            if event.type == python.QUIT:
                return
        pygame.Surface.fill(screen, (1,1,1))
        pygame.display.flip()

if __name__ == "__main__":
    main()