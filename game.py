import pygame
import sys
from random import randint

pygame.init()
game_font = pygame.font.Font(None, 30)

screen_width, screen_height = 800, 600
screen_fill_color = (32, 52, 71)
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Alien Pyshooter")

fighter_image = pygame.image.load("images/fighter.png")
rocket_image = pygame.image.load("images/rocket.png")
alien_image = pygame.image.load("images/alien.png")
stars_image = pygame.image.load("images/stars2.png")



FIGHTER_STEP = 5
fighter_width, fighter_height = fighter_image.get_size()
fighter_x = screen_width / 2 - fighter_width / 2
fighter_y = screen_height - fighter_height
fighter_is_moving_left = False
fighter_is_moving_right = False


ROCKET_STEP = 3
rocket_width, rocket_height = rocket_image.get_size()
rocket_x = fighter_x + fighter_width / 2 - rocket_width / 2
rocket_y = fighter_y - rocket_height
rocket_was_fired = False


ALIEN_STEP = 0.3
alien_speed = ALIEN_STEP
alien_width, alien_height = alien_image.get_size()
alien_x = randint(0, screen_width - alien_width)
alien_y = 0

game_score = 0

game_is_running = True
while game_is_running:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         sys.exit()
      
      if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_LEFT:
            fighter_is_moving_left = True

         elif event.key == pygame.K_RIGHT:
            fighter_is_moving_right = True

         elif event.key == pygame.K_SPACE:
            rocket_was_fired = True
            rocket_x = fighter_x + fighter_width / 2 - rocket_width / 2
            rocket_y = fighter_y - rocket_height

      elif event.type == pygame.KEYUP:
         if event.key == pygame.K_LEFT:
            fighter_is_moving_left = False
         elif event.key == pygame.K_RIGHT:
            fighter_is_moving_right = False

         
   if fighter_is_moving_left and fighter_x >= FIGHTER_STEP:
      fighter_x -= FIGHTER_STEP  
   elif fighter_is_moving_right and fighter_x <= screen_width - fighter_width - FIGHTER_STEP: 
      fighter_x += FIGHTER_STEP
   
   alien_y += alien_speed

   if rocket_was_fired and rocket_y + rocket_height < 0:
      rocket_was_fired = False
   elif rocket_was_fired:
      rocket_y -= ROCKET_STEP



   screen.fill(screen_fill_color)
   screen.blit(stars_image, (20, 20))
   screen.blit(fighter_image, (fighter_x, fighter_y))
   screen.blit(alien_image, (alien_x, alien_y))


   
   if rocket_was_fired:
      screen.blit(rocket_image, (rocket_x, rocket_y))

   game_score_text = game_font.render(f"Your score: {game_score}", True, 'yellow')
   screen.blit(game_score_text, (20, 20))

   pygame.display.update()

   if alien_y + alien_height > fighter_y:
      game_is_running = False


   if rocket_was_fired and \
         alien_x < rocket_x < alien_x + alien_width - rocket_width and \
         alien_y < rocket_y < alien_y + alien_height - rocket_height:
      rocket_was_fired = False
      alien_x = randint(0, screen_width - alien_width)
      alien_y = 0
      alien_speed += ALIEN_STEP
      game_score += 1
      

game_over_text = game_font.render("Game Over :(", True, 'red')
game_over_rectangle = game_over_text.get_rect()
game_over_rectangle.center = (screen_width / 2, screen_height / 2)
screen.blit(game_over_text, game_over_rectangle)
pygame.display.update()
pygame.time.wait(5000)
