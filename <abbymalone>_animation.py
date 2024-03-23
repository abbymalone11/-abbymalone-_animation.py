#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 20:30:49 2024

@author: abbymalone
"""


import pygame

def main():
    pygame.init()

   
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Kachow!")

 
    background = pygame.image.load("Raceway.jpg")
    background = background.convert_alpha()
    background = pygame.transform.scale(background, screen.get_size())
   
   
    cardinal = pygame.image.load("Lightning_mcqueen.jpg")
    cardinal = cardinal.convert_alpha()
    cardinal = pygame.transform.scale(cardinal, (100, 100))

    
    cardinal_x = 0
    cardinal_y = 200

    

        
    clock = pygame.time.Clock()
    keepGoing = True

        
    while keepGoing:

        
        clock.tick(30)

       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False

        
        cardinal_x += 5
        if cardinal_x > screen.get_width():
            cardinal_x = 0

        
        screen.blit(background, (0, 0))
        screen.blit(cardinal, (cardinal_x, cardinal_y))
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()