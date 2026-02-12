import random
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

#define font
font = pygame.font.SysFont('bauhaus 93',  60)

# define colours
white = (255,255,255)

# define game vari
ground_scroll = 0
scroll_speed = 4
flying_bird = False
game_over = False
pipe_gap = 150
pipe_freq = 1500 # milliseconds
last_pipe = pygame.time.get_ticks() - pipe_freq
score= 0
pass_pipe = False



# LOad images 
bg = pygame.image.load('Flappy_bird/img/bg.png')
ground_img = pygame.image.load('Flappy_bird/img/ground.png')

# draw text to image function
def draw_text(text, font, text_col, x,y):
  img = font.render(text,True, text_col)
  screen.blit(img,(x,y))


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
    self.vel = 0
    self.clicked =  False

  def update(self):
    if flying_bird == True:
  # gravity - velocity handler in animation
      self.vel +=0.5
      if self.vel > 8 :
        self.vel = 8
      if self.rect.bottom < 768:
        self.rect.y += int(self.vel)

# jump  - physics 
# here, cataching the Space-bar being clicked 
    if game_over == False:
      keys =pygame.key.get_pressed() 
      if keys[pygame.K_SPACE] and self.clicked == False:
        self.clicked = True
        self.vel = -10
        # here , catching the Space-bar being realsed 
      if not keys[pygame.K_SPACE] == 0 :
        self.clicked = False




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


  # Rotate the bird img
      self.image =  pygame.transform.rotate(self.images[self.index],self.vel * -2)
    else: 
      self.image = pygame.transform.rotate(self.images[self.index],-90)


# Adding pipes in game!
class pipe(pygame.sprite.Sprite):
  def __init__(self, x,y, position):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load('Flappy_bird/img/pipe.png')
    self.rect = self.image.get_rect()   # takes the image and create boundary around it 
    # position 1 is from the top -1 is from the bottom
    if position == 1:
      self.image = pygame.transform.flip(self.image, False , True)
      self.rect.bottomleft =[x,y - int(pipe_gap/2)]
    if position == -1:
      self.rect.topleft =[x,y + int(pipe_gap /2)]

  def update(self):
    self.rect.x -= scroll_speed
    if self.rect.right < 0:
      self.kill()
# cREATE A GROUP
bird_group = pygame.sprite.Group()
pipe_group = pygame.sprite.Group()

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
  
  pipe_group.draw(screen)

  
  # draw ground!!
  screen.blit(ground_img,(ground_scroll,768))
  
  
  # check the score! -> score_board build logic
  if len(pipe_group) > 0:     #this group is like a list so, i can acess each individual like in list 
    if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.left\
      and bird_group.sprites()[0].rect.right < pipe_group.sprites()[0].rect.right\
      and pass_pipe == False:
      pass_pipe = True
    if pass_pipe == True:   # Leaving the pipe area 
      if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.right:
        score +=1
        pass_pipe = False
  # so right now the score is on the text format in the terminal , we need to convert the text into the img and then .blit() to draw the img on app.
  
  
  draw_text(str(score), font, white, int(screen_width /2),20)
  
  # look for collision
  if pygame.sprite.groupcollide(bird_group, pipe_group, False, False) or flappy.rect.top< 0:
    game_over =True


  # check if bird hit colllision 
  if flappy.rect.bottom >= 768:
    game_over = True
    flying_bird= False



  if game_over == False  and flying_bird == True:
  # gernate the pipe 
    time_now = pygame.time.get_ticks()
    if time_now - last_pipe > pipe_freq:
      pipe_height = random.randint(-100,100)
      # instance of pipe
      btm_pipe = pipe(screen_width, int(screen_height / 2)  + pipe_height,-1)  
      top_pipe = pipe(screen_width, int(screen_height / 2)+ pipe_height,1)  # flip version of bottom pipe
      pipe_group.add(btm_pipe)
      pipe_group.add(top_pipe)
      last_pipe = time_now


  # Draw and scroll the ground
    ground_scroll -= scroll_speed
    if abs(ground_scroll)>35:
      ground_scroll =0
      
    pipe_group.update()   # for stopping the pipe to move when the game_over = true

  for event in pygame.event.get(): 		# the only event that  is happening 
    if event.type == pygame.QUIT:run = False		# this for quitting 
    if event.type ==pygame.KEYDOWN and event.key== pygame.K_SPACE and flying_bird == False and game_over == False:
      flying_bird = True


  pygame.display.update()

pygame.quit()