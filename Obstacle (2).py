import pygame  
from Configuration import SCREEN_WIDTH, GAME_SPEED, SCREEN

# Obstacle.py


class Obstacle:
    def __init__(self, image, type):
        # The image is a list and the type is the index to select which sprite to use in the list
        self.image = image
        self.type = type

        # Create a rect using the image type that was selected and start position 
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self):
        # Move object to left to create motion 
        self.rect.x -= GAME_SPEED

        # If object is on the screen = True else it is false if off
        return self.rect.right > 0

    def draw(self, SCREEN):
        # Draws the object 
        SCREEN.blit(self.image[self.type], self.rect)

