import pygame
import random, time

BLACK = pygame.color.THECOLORS['black']
WHITE = pygame.color.THECOLORS['white']
BLUE = pygame.color.THECOLORS['darkblue']
GREEN = pygame.color.THECOLORS['darkgreen']
RED = pygame.color.THECOLORS['darkred']
PURPLE = pygame.color.THECOLORS['purple']
YELLOW = pygame.color.THECOLORS['yellow']

alien='kosmita.png'
alien1='alien1.png'
coin = 'coin.png'
background = pygame.image.load("stars.png")
done = False
screen_width = 1280
screen_height = 720


pygame.init()
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption('Game')
clock = pygame.time.Clock()
 
 
class Wall(pygame.sprite.Sprite):
 
 
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
 
 
class Player(pygame.sprite.Sprite):

    change_x = 0
    change_y = 0
 
    def __init__(self, x, y):
   
        super().__init__()
        self.image = pygame.image.load(alien)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
 
    def changespeed(self, x, y):
   
        self.change_x += x
        self.change_y += y
 
    def move(self, walls):
 
       
        self.rect.x += self.change_x
 
        
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right
 
       
        self.rect.y += self.change_y
 
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom


class Enemy(pygame.sprite.Sprite):

    def __init__(self, x, y, speed, typeenemy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(alien1)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.enemyspeed = speed
        self.enemytype = typeenemy
        if self.enemytype == 1:
            self.enemydirup = 1
            self.enemydirdown = 0
        elif self.enemytype == 2:
            self.enemydirup = 0
            self.enemydirdown = 1
            self.enemydirright = 0
            self.enemydirleft = 0
        elif self.enemytype == 3:
            self.enemydirright = 1
            self.enemydirleft = 0

   
    def update(self, walls):

        if self.enemytype == 1:
            if self.enemydirup == 1:
                if pygame.sprite.spritecollide(self, walls, False):
                    self.enemydirup = 0
                    self.enemydirdown = 1
                    self.rect.y -= self.enemyspeed 
                else:
                    self.rect.y += self.enemyspeed
            elif self.enemydirdown == 1:
                if pygame.sprite.spritecollide(self, walls, False):
                    self.enemydirup = 1
                    self.enemydirdown = 0
                    self.rect.y += self.enemyspeed
                else:
                    self.rect.y -= self.enemyspeed          
        elif self.enemytype == 2:
            if self.enemydirdown == 1:
                if pygame.sprite.spritecollide(self, walls, False):
                    self.enemydirright = 1
                    self.enemydirdown = 0
                else:
                    self.rect.y += self.enemyspeed
            elif self.enemydirright == 1:
                if self.rect.x == 635:
                    self.enemydirup = 1
                    self.enemydirright = 0
                    self.rect.y -= self.enemyspeed
                else:
                    self.rect.x += self.enemyspeed
            elif self.enemydirup == 1:
                if pygame.sprite.spritecollide(self, walls, False):
                    self.enemydirleft = 1
                    self.enemydirup = 0
                    self.rect.x -= self.enemyspeed
                else:
                    self.rect.y -= self.enemyspeed
            elif self.enemydirleft == 1:
                if self.rect.x == 535:
                    self.enemydirdown = 1
                    self.enemydirleft = 0
                    self.rect.y += self.enemyspeed
                else:
                    self.rect.x -= self.enemyspeed
        elif self.enemytype == 3:
            if self.enemydirright == 1:
                if pygame.sprite.spritecollide(self, walls, False):
                    self.enemydirright = 0
                    self.enemydirleft = 1
                    self.rect.x -= self.enemyspeed 
                else:
                    self.rect.x += self.enemyspeed
            elif self.enemydirleft == 1:
                if pygame.sprite.spritecollide(self, walls, False):
                    self.enemydirright = 1
                    self.enemydirleft = 0
                    self.rect.x += self.enemyspeed
                else:
                    self.rect.x -= self.enemyspeed
        

        
 
    
class Coin(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
      
        self.image = pygame.image.load(coin)
        self.rect = self.image.get_rect()
    

 
class Room(pygame.sprite.Sprite):
    
    
    def __init__(self):
        self.wall_list = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()
        coins_list = pygame.sprite.Group()
        
    def aktualizcja(screen, score):
        global life
        global win
        coins_hit_list = pygame.sprite.spritecollide(player, coins_list, True)
        screen.blit(background, [0, 0])
        for coins in coins_hit_list:
            score.text += 1
            score.sett([500,50])
        score.draw(screen)
        if score.text == 50:
            win = 1
            
        enemyattack = pygame.sprite.spritecollide(player, enemysprites, False)
        
        if enemyattack:
            life = 0
        enemy.update(room.wall_list)
        enemy2.update(room.wall_list)
        enemy3.update(room.wall_list)
        enemy4.update(room.wall_list)
    pygame.display.flip()
   
            
        
 
class Room1(Room):
  
    def __init__(self):
        super().__init__()
    
        walls = [[0, 0, 20, 720, WHITE],
                 [1260, 0, 20, 720, WHITE],
                 [20, 0, 1260, 20, WHITE],
                 [20, 700, 1260, 20, WHITE]
                ]
      
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)
 
        for x in range(100, 1280, 200):
            for y in range(90, 450, 310):
                wall = Wall(x, y, 20, 220, BLUE)
                self.wall_list.add(wall)

        for x in range(200, 1180, 200):
            wall = Wall(x, 150, 20, 400, WHITE)
            self.wall_list.add(wall)
        
            
        movecoinx = 0
        movecoiny = 0
        
   
        i = 0
        while i < 50:
            coins = Coin()
            i += 1
            if movecoinx or movecoiny < 1:
                coins.rect.x = random.randrange(1230)
                coins.rect.y = random.randrange(680)
            else:
                if movecoinx < 0:
                    coins.rect.x -= 5
                elif movecoinx > 0:
                    coins.rect.x += 5
                if movecoiny < 0:
                    coins.rect.y -= 5
                elif movecoiny > 0:
                    coins.rect.y += 5

            hit = pygame.sprite.spritecollide(coins, self.wall_list, False)
            hit2 = pygame.sprite.spritecollide(coins, coins_list, False)
            if hit or hit2:
                if coins.rect.x < 0:
                    movecoinx = 5
                elif coins.rect.x >= 0:
                    movecoinx = -5
                if coins.rect.y < 0:
                    movecoiny = 5
                elif coins.rect.y >= 0:
                    movecoiny = -5
                i -= 1
                    
            else:
                coins_list.add(coins)
                movecoinx = 0
                movecoiny = 0
            
 
class Text:
    def __init__(self, text, color, position, size = 100):
        self.text = text
        self.color = color
        self.font = pygame.font.SysFont(None, size)
        self.sett(position)
        
        

    def sett(self, position):
        self.image = self.font.render(str(self.text), 1,
                                      self.color)
        self.rect = self.image.get_rect()
        self.rect.center =position
        

    def draw(self,surface):
        surface.blit(self.image, self.rect)
      

def GgameOver():
    gameover = Text(0,YELLOW, [400, 35], 150)
    gameover.text = "GAME OVER"
    gameover.sett([screen_width//2, screen_height//2])
    gameover.draw(screen)

def WinGame():
    score.text = "THIS IS THE END . . . "
    score.sett([screen_width//2, screen_height//2])
    score.draw(screen)
        

   

 
# 
player = Player(30, 320)
enemy = Enemy(135, 320, 2, 1)
enemy2 = Enemy(535, 25, 5, 2)
enemy3 = Enemy(935, 30, 3, 1)
enemy4 = Enemy(1030, 325, 4, 3)

score = Text(0,YELLOW, [500, 50])
coins_list = pygame.sprite.Group()

movingsprites = pygame.sprite.Group()
enemysprites = pygame.sprite.Group()
movingsprites.add(player)
enemysprites.add(enemy)
enemysprites.add(enemy2)
enemysprites.add(enemy3)
enemysprites.add(enemy4)

rooms = []
room = Room1()
rooms.append(room)
 
life = 1
win = 0





 
while not done:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-5, 0)
            if event.key == pygame.K_RIGHT:
                player.changespeed(5, 0)
            if event.key == pygame.K_UP:
                player.changespeed(0, -5)
            if event.key == pygame.K_DOWN:
                player.changespeed(0, 5)
 
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(5, 0)
            if event.key == pygame.K_RIGHT:
                player.changespeed(-5, 0)
            if event.key == pygame.K_UP:
                player.changespeed(0, 5)
            if event.key == pygame.K_DOWN:
                player.changespeed(0, -5)
 
      
    if life:
        if win == 1:
            WinGame()
        else:
            player.move(room.wall_list)
            Room.aktualizcja(screen, score)
            room.wall_list.draw(screen)
            movingsprites.draw(screen)
            enemysprites.draw(screen)
            coins_list.draw(screen)
    else:
        GgameOver()

    clock.tick(60)
    pygame.display.flip()
 
pygame.quit()
 

