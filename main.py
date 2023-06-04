from curses import window
import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join
pygame.init() #initialise pygame

pygame.display.set_caption("Python platformer") #sets caption at top of window

BG_COLOR = (255, 255, 255)#set background colour
WIDTH, HEIGHT = 1000, 800 #dimensions of the display. make this a bit smaller for smaller sized screens
FPS = 60 #frames per second
PLAYER_VEL = 5 #player velocity, speed which player moves around screen

window = pygame.display.set_mode((WIDTH, HEIGHT))

#inside of main, run event loops (ie whats hanlding the collisions etc.)
def main(window):
    clock = pygame.time.Clock()

    #set a while loop to run continuously
    run = True
    while run:
        clock.tick(FPS) #ensures the while loop will only run "FPS" times per second, ie 60 times per second. regulates frame rate across devices

        for event in pygame.event.get():
            #check if user quits the game
            if event.type == pygame.QUIT:
                run = False
                break

    pygame.quit()
    quit()


#only call the main function if we run the file directly
if __name__ == "__main__":
    main(window)