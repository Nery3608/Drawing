import pygame

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Drawing Objects")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
ORANGE = (255, 128, 0)

display_surface.fill(WHITE)

CENTER = (300, 300)
RADIUS = 100
pygame.draw.circle(display_surface, YELLOW, CENTER, RADIUS, 55)

CENTER = (300, 300)
RADIUS = 100
pygame.draw.circle(display_surface, ORANGE, CENTER, RADIUS, 25)

START = (25, 25)
END = (25, 800)
pygame.draw.line(display_surface, BLACK, START, END, 100)


START = (25, 25)
END = (800, 25)
pygame.draw.line(display_surface, BLACK, START, END, 100)

START = (25, 800)
END = (25, 800)
pygame.draw.line(display_surface, BLACK, START, END, 100)

















running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

pygame.quit()