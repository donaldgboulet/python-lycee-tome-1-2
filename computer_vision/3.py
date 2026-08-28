import pygame
pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Test Pygame!")
screen.fill((0, 128, 255))
pygame.display.flip()
pygame.time.wait(3000)
pygame.quit()