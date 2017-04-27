import pygame
import sys
from pygame.locals import *

# Set up pygame
pygame.init()

# ----- START OF EXPERIMENT -----
# What happens when you change the following variables?

# Screen size format is (width, height)
screenSize = (600, 400)

caption = "Hello world!"
textString = "Hello world!"
textSize = 64

# Color format is (red, green, blue), where red, green, blue can have values from 0-255
textColor = (255, 255, 255)
textBackground = (0, 0, 255)

# ----- END OF EXPERIMENT -----

# Set up the window
windowSurface = pygame.display.set_mode(screenSize, 0, 32)
windowSurface.fill((255, 255, 255))

# Set the window's caption
pygame.display.set_caption(caption)

# Set up the text
basicFont = pygame.font.SysFont(None, textSize)
text = basicFont.render(textString, True, textColor, textBackground)
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

# Draw the text
windowSurface.blit(text, textRect)

# Draw the window onto the screen
pygame.display.update()

# Run the event loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
