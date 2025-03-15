import pygame
from player import Player
from constants import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    running = True
    while (running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (1,1,1))
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()
        clock.tick(60)
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()