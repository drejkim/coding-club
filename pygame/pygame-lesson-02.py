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
# circleColor = ??
# circlePosition = ??
# circleRadius = ??

# pygame.draw.circle(windowSurface, circleColor, circlePosition, circleRadius)

# --- TODO: Create a line
# lineColor = ??
# lineStartPoint = ??
# lineEndPoint = ??

# pygame.draw.line(windowSurface, lineColor, lineStartPoint, lineEndPoint)

# --- TODO: Create a rectangle
# rectColor = ??
# rectVertices = ??

# pygame.draw.polygon(windowSurface, rectColor, rectVertices)

# ----- END OF EXPERIMENT -----

# Draw the window onto the screen
pygame.display.update()

# Run the event loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()