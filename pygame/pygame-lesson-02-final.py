import pygame
import sys
from pygame.locals import *

# Set up pygame
pygame.init()

# Set up the window
screenSize = (800, 600)
windowSurface = pygame.display.set_mode(screenSize, 0, 32)
windowSurface.fill((255, 255, 255))

# Set the window's caption
caption = "Shapes!"
pygame.display.set_caption(caption)

# ----- START OF EXPERIMENT -----
# Remember: Colors are a tuple of 3 integers (red, green, blue), where red, green, blue can have values from 0-255

# --- TODO: Create a circle
circleColor = (0, 255, 0)
circlePosition = (400, 300)
circleRadius = 80

pygame.draw.circle(windowSurface, circleColor, circlePosition, circleRadius)

# --- TODO: Create a line
lineColor = (0, 0, 0)
lineStartPoint = (30, 20)
lineEndPoint = (400, 80)

pygame.draw.line(windowSurface, lineColor, lineStartPoint, lineEndPoint)

# --- TODO: Create a rectangle
rectColor = (0, 0, 255)
rectVertices = (
    (10, 10),
    (250, 10),
    (250, 100),
    (10, 100)
)

pygame.draw.polygon(windowSurface, rectColor, rectVertices)

# ----- END OF EXPERIMENT -----

# Draw the window onto the screen
pygame.display.update()

# Run the event loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()