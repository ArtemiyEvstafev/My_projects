def DrawHouse(a, b, HouseColor, RoofColor, HouseSize):
    global WindowColor
    pygame.draw.rect(screen, HouseColor, (a, b - HouseSize, HouseSize, HouseSize))
    pygame.draw.rect(screen, (0, 0, 0), (a, b - HouseSize, HouseSize, HouseSize), 5)

    pygame.draw.polygon(screen, RoofColor, ((a, b - HouseSize), (a + HouseSize / 2, b - HouseSize * 1.5), (a + HouseSize, b - HouseSize)))
    pygame.draw.polygon(screen, (0, 0, 0), ((a, b - HouseSize), (a + HouseSize / 2, b - HouseSize * 1.5), (a + HouseSize, b - HouseSize)), 5)
    WindowSize = HouseSize // 3
    pygame.draw.rect(screen, WindowColor, (a + WindowSize, b - WindowSize * 2, WindowSize, WindowSize))
    pygame.draw.line(screen, (0, 0, 0), (a + WindowSize, b - WindowSize), (a + WindowSize, b - WindowSize * 2), 7)
    pygame.draw.line(screen, (0, 0, 0), (a + WindowSize * 2, b - WindowSize), (a + WindowSize * 2, b - WindowSize * 2), 7)
    pygame.draw.line(screen, (0, 0, 0), (a + WindowSize * 1.5, b - WindowSize), (a + WindowSize * 1.5, b - WindowSize * 2), 7)
    pygame.draw.line(screen, (0, 0, 0), (a + WindowSize, b - WindowSize), (a + WindowSize * 2, b - WindowSize), 7)
    pygame.draw.line(screen, (0, 0, 0), (a + WindowSize, b - WindowSize * 2), (a + WindowSize * 2, b - WindowSize * 2), 7)
    pygame.draw.line(screen, (0, 0, 0), (a + WindowSize, b - WindowSize * 1.5), (a + WindowSize * 2, b - WindowSize * 1.5), 7)


import pygame
import random
WindowColor = (255, 231, 77)
SkyColor = (24, 28, 61)
GrassColor = (18, 64, 30)
screen = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("Light up a star!")
screen.fill(SkyColor)
a = random.randint(1, 10)
c = []
for i in range(a):
    c.append(random.randint(350, 450))
c.sort(reverse=False)
pygame.draw.rect(screen, GrassColor, (0, 300, 1000, 500))
stars = []
for i in c:
    DrawHouse(random.randint(-50, 950), i, (random.randint(0, 100), random.randint(0 , 100), random.randint(0, 100)), (random.randint(0, 100), random.randint(0 , 100), random.randint(0, 100)), random.randint(30, 200))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if screen.get_at(event.pos) == SkyColor:
                    pygame.draw.circle(screen, (255, 255, 255), event.pos, random.randint(2, 8))
    pygame.display.update()

pygame.display.update()
pygame.time.wait(20000)
