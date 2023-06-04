from curses import window
import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join
pygame.init() #initialise pygame

pygame.display.set_caption("Python platformer") #sets caption at top of window

#BG_COLOR = (255, 255, 255)#set background colour
WIDTH, HEIGHT = 1000, 800 #dimensions of the display. make this a bit smaller for smaller sized screens
FPS = 60 #frames per second
PLAYER_VEL = 5 #player velocity, speed which player moves around screen

window = pygame.display.set_mode((WIDTH, HEIGHT))



def get_background(name):
    image = pygame.image.load(join("assets", "Background", name))
    _, _, width, height = image.get_rect() #get dimensions of the image width and height
    tiles = [] #start a tiles list 

    for i in range(WIDTH // width + 1): #finds about how many tiles are needed to fill the screen, plus 1 so theres no gaps
        for j in range (HEIGHT // height + 1): #same again but in the height direction
            pos = (i * width, j * height) #denote top left hand corner of the current tile added to the list
            tiles.append(pos)
    return tiles, image


#setup function to draw the background
def draw(windown, background, bg_image):
    for tile in background:
        window.blit(bg_image, tile)

    pygame.display.update()

#inside of main, run event loops (ie whats hanlding the collisions etc.)
def main(window):
    clock = pygame.time.Clock()
    background, bg_image = get_background("Blue.png")

    #set a while loop to run continuously
    run = True
    while run:
        clock.tick(FPS) #ensures the while loop will only run "FPS" times per second, ie 60 times per second. regulates frame rate across devices

        for event in pygame.event.get():
            #check if user quits the game
            if event.type == pygame.QUIT:
                run = False
                break

        draw(window, background, bg_image)

    pygame.quit()
    quit()


#only call the main function if we run the file directly
if __name__ == "__main__":
    main(window)