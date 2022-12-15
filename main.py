import pygame

pygame.init()
width = 500
height = 500
pygame.display.set_mode((width,height))
pygame.display.set_caption("Tic-Tac-Toe")


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()


