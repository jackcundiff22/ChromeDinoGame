import pygame
import random
from Obstacle import Obstacle

# Cactuses.py

class SmallCactus(Obstacle):
  def __init__(self, image):
      # Randomly chooses between the two small cactuses 
      self.type = random.randint(0, 2)
      
      # Intializes the base obstacle class with the image and type that is selected 
      super().__init__(image, self.type)
      
      # Sets vertical postion of cactuses 
      self.rect.y = 325


class LargeCactus(Obstacle):
  def __init__(self, image):
      # Randomly chooses between the two large cactuses 
      self.type = random.randint(0, 2)
      
      super().__init__(image, self.type)
      
      self.rect.y = 300