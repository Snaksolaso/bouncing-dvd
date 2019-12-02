import pygame
import dvd
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
running = True
screen.fill((0, 0, 0))
clock = pygame.time.Clock()
timesince = clock.tick(90)
pygame.display.flip()
dvd = dvd.dvd(height, width)
direction = 0

while(running):
    clock.tick(90)
    direction = dvd.update(direction, screen)
    




