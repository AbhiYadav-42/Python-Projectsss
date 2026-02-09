import pygame
from pygame.locals import *

pygame.init()

clock =  pygame.time.Clock()
fps =60     # frame rate 

# game window
screen_width  = 864
screen_height =936

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Flappy Bird')

# define game vari
ground_scroll = 0
scroll_speed = 4

# LOad images 
bg = pygame.image.load('Flappy_bird/img/bg.png')
ground_img = pygame.image.load('Flappy_bird/img/ground.png')


class Bird(pygame.sprite.Sprite):
  def __init__(self,x,y):
    pygame.sprite.Sprite.__init__(self)
    self.images =[]     # empty list use for transition of images which will act as an animation of a bird 
    self.index = 0      # this is for images order, which will be shown after which one  
    self.counter = 0    # this for the speed , like how the animation speed it going to be 
    for num in range(1,4):
      img = pygame.image.load(f'Flappy_bird/img/bird{num}.png')
      self.images.append(img)
    self.image = self.images[self.index]
    self.rect = self.image.get_rect()     # create a rectangle
    self.rect.center = [x,y]


  def update(self):
    # handle the animation of bird 
    self.counter +=1
    flap_cooldown = 5
    
    if self.counter > flap_cooldown:
      self.counter = 0
      self.index +=1
# this if statement will maintain the bird animation by resetting the img-count to 0 
      if self.index >= len(self.images):
        self.index = 0 
    self.image = self.images[self.index]


# cREATE A GROUP
bird_group = pygame.sprite.Group()

flappy = Bird(100,int(screen_height / 2 ))    # putting the Bird in the position according to the coordinates 

bird_group.add(flappy)

# Game LOOP-
run = True
while run:

  clock.tick(fps)

# Daw background
  screen.blit(bg,(0,0))		
#blit is for showing images on to the screen 

  bird_group.draw(screen)
  bird_group.update()


# Draw and scroll the ground
  screen.blit(ground_img,(ground_scroll,768))
  ground_scroll -= scroll_speed
  if abs(ground_scroll)>35:
    ground_scroll =0
  
  for event in pygame.event.get(): 		# the only event that  is happening 
    if event.type == pygame.QUIT:run = False		# this for quitting 
  
  pygame.display.update()

pygame.quit()