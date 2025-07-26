import pygame
from Configuration import DINO_JUMP_IMG, DINO_DUCKING_IMGS, DINO_RUNNING_IMGS, SCREEN

# Player1.py (Dinosaur File)

class Dinosaur:
    # Set Dinosaur Position on Track and Jump Height and Duck Height
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_HEIGHT = 8.5

    def __init__(self, run_imgs, jump_img, duck_imgs, jump_sound):

        # Load images and Intilaize Dinosaur traits to use later
        self.duck_imgs = [pygame.image.load(img) for img in DINO_DUCKING_IMGS]
        self.jump_img = pygame.image.load(DINO_JUMP_IMG)
        self.run_imgs = [pygame.image.load(img) for img in DINO_RUNNING_IMGS]

        self.jump_sound = jump_sound
       
        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.step_index = 0
        self.jump_height = self.JUMP_HEIGHT

        # Sets the orginal image and postions the rect
        self.image = self.run_imgs[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

    def update(self, userInput):
        if self.dino_jump:
            self.jump()
        elif self.dino_duck:
            self.duck()
        else:
            self.run()
        # Reset the animation after 10 steps (for proper frame rate adjustments)
        if self.step_index >= 10:
            self.step_index = 0

        # Key presses for Jump and Duck
        if userInput[pygame.K_UP] and not self.dino_jump:
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True
            self.jump_sound.play()
        elif userInput[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
        elif not (self.dino_jump or userInput[pygame.K_DOWN]):
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False

    def duck(self):
        # Change the orginal image to ducking and update a new rect position
        self.image = self.duck_imgs[self.step_index // 5] # Cycles between two ducking frames
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        self.step_index += 1

    def run(self):
        # Change the orginal image to running and update a new rect position 
        self.image = self.run_imgs[self.step_index // 5] # Cycles between two running frames
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    def jump(self):
        # Intialize Jumping Logical factors (aka gravity)
        self.image = self.jump_img
        if self.dino_jump:
            self.dino_rect.y -= self.jump_height * 4 # Goes up
            self.jump_height -= 0.8  # Applies Gravity 
        if self.jump_height < -self.JUMP_HEIGHT:
            # End jump and reset 
            self.dino_jump = False
            self.jump_height = self.JUMP_HEIGHT

    def draw(self, SCREEN):
        # Render dino 
        SCREEN.blit(self.image, self.dino_rect)