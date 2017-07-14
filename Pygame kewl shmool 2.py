import pygame
import random
import os import path

WIDTH = 480
HEIGHT = 600
FPS = 30

#define colours
WHITE = (225, 225, 225)
BLACK = (0, 0, 0)
RED = (225, 0, 0)
GREEN = (0, 225, 0)
BLUE = (0, 0, 225)

#set up image folder
img_folder = path.join(path.dirname(__file__), 'img')


class Player(pygame.sprite.Sprite):
#sprite for player
    def __init__(self): #initialises sprite
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect() #rect = rectangle = sprite
        self.rect.centerx = (WIDTH/2) #centers sprite
        self.rect.bottom=HEIGHT-10
        self.speedx=0

    def shoot(self):
        bullet = Bullet (self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullet.add(bullets)
        

    def update(self):
        self.speedx=0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        elif keystate [pygame.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        elif self.rect.left < 0:
            self.rect.left = 0

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = mob_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x =  random.randrange (WIDTH - self.rect.width)
        self.rect.y = random.randrange (-100, -40)
        self.speedy = random.randrange (1, 8)
        self.speedx = random.randrange (-2, 2)
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left > WIDTH or self.rect.right < 0:
            self.rect.x =  random.randrange (WIDTH - self.rect.width)
            self.rect.y = random.randrange (-100, -40)
            self.speedy = random.randrange (1, 8)
            self.speedx = random.randrange (-2, 2)

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
            pygame.sprite.Sprite.__init__(self)
            self.image = bullet.img
            self.image.set_colorkey(BLACK)
            self.rect = self.image.get_rect()
            self.rect.bottom = y
            self.rect.centerx = x
            self.speedy = -10
    def update(self):
            self.rect.y += self.speedy
            if self.rect.bottom < 0:
                self.kill()
        
        
                                  
#initialize pygame and create window
pygame.init()
pygame.mixer.init() #enables sound
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Kewl Shmool") #names the game
clock = pygame.time.Clock()  #keeps track of time

#load images
player_img = pygame.image.load(path.join(img_dir, "Ship.png")).convert()
mob_img = pygame.image.load(pah.join(img_dir, "Emimie.png")).convert()
bullet_img = pygame.image.load(pah.join(img_dir, "Laser.png")).convert()

all_sprites = pygame.sprite.Group()
player = Player() #call class
all_sprites.add(player) #add sprite to group
mobs = pygame.sprite.Group()
for i in range (8):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)
bullets = pygame.sprite.Group()

#game loop 
running = True

while running:
        #keep your loop running at the right speed
    clock.tick(FPS)
        #process input
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                     if event.key == pygame.K_SPACE:
                             player.shoot()
        #update
    all_sprites.update()
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits:
            m = Mob()
            all_sprites.add(m)
            mobs.add(m)
            
    hits = pygame.sprite.spritecollide (player, mobs, False)
    if hits:
        running = False

        
                     
        #draw/render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    #after drawing everything you want to flip the dispaly
    pygame.display.flip()
pygame.quit()


