#-----------------------------------------------------------------------------
# Name:        Assignment Template (assignment.py)
# Purpose:     A description of your program goes here.
#
# Author:      Nicolas
# Created:     31-march-2025
# Updated:     13-Sept-2025
#-----------------------------------------------------------------------------
#I think this project deserves a level XXXXXX because ...
#
#Features Added:
#   ...
#   ...
#   ...
#-----------------------------------------------------------------------------

import pygame

pygame.init()
pygame.display.set_mode((800, 400))
pygame.display.set_caption("Game")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT()
    pygame.display.update()
