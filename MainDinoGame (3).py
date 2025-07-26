import pygame
import random

from Player1 import Dinosaur
from Cactuses import SmallCactus, LargeCactus
from Bird import Bird
from Cloud import Cloud
from Configuration import *

# MainDinoGame.py

# Intialize Pygame and set the title of the game
pygame.init()
pygame.display.set_caption("Dino Run!") # Title 
FONT = pygame.font.Font('freesansbold.ttf', 20) # Intialize font

# Intialize Variables 
game_speed = GAME_SPEED # Game Speed which is increased every 100 points 
x_pos_bg = 0 # Horizontal Position of background image
y_pos_bg = 380 # Vertical Position of background image 
points = 0 # Sets points to start tracking score 
obstacles = [] # List to store all the obtsacles 
death_count = 0 # Set to track number of times player has died 

# Load all Sounds
jump_sound = pygame.mixer.Sound(JUMP_SOUND)
die_sound = pygame.mixer.Sound(DIE_SOUND)
point_sound = pygame.mixer.Sound(POINT_SOUND)

# Load all images 
dino_run_imgs = [pygame.image.load(img) for img in DINO_RUNNING_IMGS]
dino_jump_img = pygame.image.load(DINO_JUMP_IMG)
dino_duck_imgs = [pygame.image.load(img) for img in DINO_DUCKING_IMGS]
cactus_small_imgs = [pygame.image.load(img) for img in CACTUS_IMAGES["small"]]
cactus_large_imgs = [pygame.image.load(img) for img in CACTUS_IMAGES["large"]]
bird_imgs = [pygame.image.load(img) for img in BIRD_IMGS]
cloud_img = pygame.image.load(CLOUD_IMG)
background_img = pygame.image.load(BACKGROUND_IMG)
game_over_img = pygame.image.load(GAMEOVER_IMG)


def score():
    global points, game_speed
    points += 1 # Increase score by 1 for each frame 
    if points % 100 == 0: # Every 100 points increase game speed 
        game_speed += 1

    blink = False  # Sets score blink to false (every 1000 points the score will blink)

    # If the score is 1000 play the point sound and blink the score 
    if points % 1000 == 0: 
        point_sound.play() 
        blink = True

    if blink and (pygame.time.get_ticks() // 100 % 2 == 0):
        return 
    
    text = FONT.render("Points: " + str(points), True, BLACK) # Renders points 
    text_rect = text.get_rect(center=(1000, 40)) # Points in top right corner 
    SCREEN.blit(text, text_rect)  # Display 


def draw_background():
    global x_pos_bg
    image_width = background_img.get_width()

    # Draws background image at current postion 
    SCREEN.blit(background_img, (x_pos_bg, y_pos_bg)) 
    
    # Draw a second background image for contionous scrolling 
    SCREEN.blit(background_img, (image_width + x_pos_bg, y_pos_bg)) 
    
    # If first image goes off screen reset it
    if x_pos_bg <= -image_width:
        x_pos_bg = 0
    x_pos_bg -= game_speed # Move background to left


def main():
    global game_speed, points, obstacles, death_count

    clock = pygame.time.Clock() # Clock to control frame rate 
    run = True
    player = Dinosaur(dino_run_imgs, dino_jump_img, dino_duck_imgs, jump_sound)
    cloud_obj = Cloud(cloud_img)
    obstacles = [] # Reset Obstacle List
    points = 0 # Reset points 
    game_speed = GAME_SPEED # Reset speed 

    spawn_delay = 0

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Exit game if window closes 
                run = False
                pygame.quit()
                exit()
            # Exit game if user presses escape key 
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: 
                run = False 
                pygame.quit()
                exit()
                

        SCREEN.fill(WHITE) # Fill screen with white background 
        user_input = pygame.key.get_pressed() # Get keys 

        draw_background() # Draw scrolling background 

        cloud_obj.draw(SCREEN) # Draw clouds 
        cloud_obj.update() # Update position 

        player.draw(SCREEN) # Draw player 
        player.update(user_input) # Update positon based on user input 

        # Creates new obstacles if there are none 
        if spawn_delay == 0:
            choice = random.randint(0, 2) # Randomly chooses between bird or cactus 
            if choice == 0:
                obstacles.append(SmallCactus(cactus_small_imgs)) # add small cactus
            elif choice == 1:
                obstacles.append(LargeCactus(cactus_large_imgs)) # add large cactus 
            else:
                obstacles.append(Bird(bird_imgs)) # Add a bird 
            spawn_delay = 60 

        # Manages obstacles and draws, upadtes and checks collisions 
        new_obstacles = []
        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            if obstacle.update():  
               new_obstacles.append(obstacle)

            # Checks if player collides with obstacle 
            if player.dino_rect.colliderect(obstacle.rect):
               die_sound.play()
               pygame.time.delay(1500) # Pauses game for a moment 
               death_count += 1
               menu(death_count) # Show game over screen and reset the game 
        obstacles = new_obstacles # Updates Obstacle List 
        spawn_delay -= 1
        score() # Update and Display score 

        clock.tick(FPS) # Set frame rate 
        pygame.display.update() # Update display 


def menu(death_count):
    global points
    run = True
    while run:
        SCREEN.fill(WHITE)
        if death_count == 0:
            message = "Press any Key to Start" # Starting message game 
            # Loads dino image 
            dino_img = pygame.image.load(DINO_RUNNING_IMGS[0])
            SCREEN.blit(dino_img,(SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT // 2 - 140))
        else:
            message = "Press any Key to Restart" # Message when dead 
            score_text = FONT.render("Your Score: " + str(points), True, BLACK)

            # Position of text and draw for end score 
            score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)) 
            SCREEN.blit(score_text, score_rect)

            SCREEN.blit(game_over_img, (SCREEN_WIDTH // 2 - game_over_img.get_width() // 2, SCREEN_HEIGHT // 2 - 200))
        
        text = FONT.render(message, True, BLACK)
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        SCREEN.blit(text, text_rect)
        
        pygame.display.update() # Update the screen 

        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Quit if window is closed 
                pygame.quit()
                run = False
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: # Exit is Escape is pressed 
                  pygame.quit()
                  run = False 
                  exit()
                else:
                  main()


if __name__ == "__main__":
    menu(death_count=0)