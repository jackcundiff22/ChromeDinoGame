import pygame

# Configuration.py
# Screen Setup
SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 600
pygame.init()
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
FPS = 30


# Set the colors that will be used
WHITE = (255,255,255)
BLACK = (0,0,0)


# Set speed of the game 
GAME_SPEED = 20

# Intilaize the sounds
JUMP_SOUND = "jump.wav"

DIE_SOUND = "die.wav"

# Every 1000 points this sound is played
POINT_SOUND = "point.wav"


# Intialize all images 

DINO_RUNNING_IMGS = ["DinoRun1.png", "DinoRun2.png"]

DINO_JUMP_IMG = "DinoJump.png"

DINO_DUCKING_IMGS = ["DinoDuck1.png", "DinoDuck2.png"]

CACTUS_IMAGES = { "small": ["SmallCactus1.png", "SmallCactus2.png", "SmallCactus3.png"],
                  "large": ["LargeCactus1.png", "LargeCactus2.png", "LargeCactus3.png"]
}

BIRD_IMGS = ["Bird1.png" , "Bird2.png"]

CLOUD_IMG = "Cloud.png"

BACKGROUND_IMG = "Track.png"

GAMEOVER_IMG = "GameOver.png"




