import pygame


class dvd:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.dvdpos = (10, 10)
        self.dvdimg = pygame.image.load("dvd3.jpg")
        self.dvdwidth = self.dvdimg.get_width()
        self.dvdheight = self.dvdimg.get_height()

    def update(self, direction, screen):
        if(direction == 0):
            x, y = self.dvdpos
            x += 2
            y += 2
            if(y + self.dvdheight >= self.height):
                direction = 1
                self.dvdpos = (x, y - 4)
            elif(x + self.dvdwidth >= self.width):
                direction = 3
            else:
                self.dvdpos = (x, y)
                screen.fill((0, 0, 0))
                screen.blit(self.dvdimg, self.dvdpos)
                pygame.display.flip()
        elif(direction == 1):
            x, y = self.dvdpos
            x += 2
            y -= 2
            if(y <= 0):
                direction = 0
            elif(x + self.dvdwidth >= self.width):
                direction = 2
            else:
                self.dvdpos = (x, y)
                screen.fill((0, 0, 0))
                screen.blit(self.dvdimg, self.dvdpos)
                pygame.display.flip()
        elif(direction == 2):
            x, y = self.dvdpos
            x -= 2
            y -= 2
            if(y <= 0):
                direction = 3
            elif(x <= 0):
                direction = 1
            else:
                self.dvdpos = (x, y)
                screen.fill((0, 0, 0))
                screen.blit(self.dvdimg, self.dvdpos)
                pygame.display.flip()
        elif(direction == 3):
            x, y = self.dvdpos
            x -= 2
            y += 2
            if(y + self.dvdheight >= self.height):
                direction = 2
            elif(x <= 0):
                direction = 0
            else:
                self.dvdpos = (x, y)
                screen.fill((0, 0, 0))
                screen.blit(self.dvdimg, self.dvdpos)
                pygame.display.flip()
        return direction