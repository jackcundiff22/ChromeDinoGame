import pygame
import random 
from Configuration import SCREEN_WIDTH, GAME_SPEED, SCREEN

# Cloud.py 

class Cloud:
  def __init__(self, image):
      # Set starting postion of Cloud off screen  to the right that has random spacing  
      self.x = SCREEN_WIDTH + random.randint(800, 1000)
      # Random Vertical Postions
      self.y = random.randint(50, 100)
      
      self.image = image 
      self.width = self.image.get_width()

  def update(self):
      # Move cloud to left based on the game speed 
      self.x -= GAME_SPEED

      # If clound moves off screen resets to right 
      if self.x < -self.width:
          self.x = SCREEN_WIDTH + random.randint(2500, 3000) # Respawns further for spacing 
          self.y = random.randint(50, 100) # Random Height 

  def draw(self, SCREEN):

      # Draw cloud
      
      SCREEN.blit(self.image, (self.x, self.y))