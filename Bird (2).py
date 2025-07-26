import pygame
from Obstacle import Obstacle
from Configuration import SCREEN

# Bird.py

class Bird(Obstacle):
  def __init__(self, image):
    self.type = 0 # Bird only has one type 
    super().__init__(image, self.type) # Intializes the obstacle base class
    self.rect.y = 250 # Vertical position for bird
    self.index = 0 # Used to alternate the wings (images) and start animation 

  def draw(self, SCREEN):
    # Loops the index if it goes above the frame count 
    if self.index >= 9:
        self.index = 0

    # Draws bird using one of the two images for wing animation 
    SCREEN.blit(self.image[self.index//5], self.rect)
    # Add index to switch to next animation frame at some point
    self.index += 1

  