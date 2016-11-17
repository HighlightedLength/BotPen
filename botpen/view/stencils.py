import math
import pygame.gfxdraw

def directed_circle(screen, x, y, theta, radius, scale, color):
    center_x = int(round(x/scale))
    center_y = int(round(screen.get_height() - y/scale))
    edge_x = int(round(x/scale + radius * math.cos(theta)))
    edge_y = int(round(screen.get_height() - y/scale + radius * math.sin(theta)))

    pygame.gfxdraw.aacircle(screen, center_x, center_y, radius, color)
    pygame.gfxdraw.line(screen, center_x, center_y, edge_x, edge_y, color)

def line(screen, x1, y1, x2, y2, scale, color):
    pygame.gfxdraw.line(
        screen,
        int(round(x1/scale)),
        int(round(screen.get_height() - y1/scale)),
        int(round(x2/scale)),
        int(round(screen.get_height() - y2/scale)),
        color)

def filled_circle(screen, x, y, r, scale, color):
    pygame.gfxdraw.filled_circle(screen,
        int(round(x/scale)),
        int(round(screen.get_height() - y/scale)), 
        r, color)
