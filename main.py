import pygame
pygame.init()
width = 500
height = 500
pygame.display.set_mode((width,height))

while True:
    for event in pygame.event.get():
        if event.type == "QUIT":
            pygame.quit()
            sys.exit()
    pygame.display.update()


