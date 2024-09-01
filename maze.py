#створи гру "Лабіринт"!
#створи гру "Лабіринт"! 
from typing import Any
from pygame import *  
'''Необхідні класи'''  
   
#клас-батько для спрайтів  
  
  
class GameSprite(sprite.Sprite):  
    #конструктор класу  
    def __init__(self, player_image, player_x, player_y, player_speed):  
        super().__init__()  
        #кожен спрайт повинен зберігати властивість image - зображення  
        self.image = transform.scale(image.load(player_image), (65, 65))  
        self.speed = player_speed  
        #кожен спрайт повинен зберігати властивість rect - прямокутник, в який він вписаний  
        self.rect = self.image.get_rect()  
        self.rect.x = player_x  
        self.rect.y = player_y  
    def reset(self):  
        window.blit(self.image, (self.rect.x, self.rect.y))  
 


class Player(GameSprite): 
    def update(self): 
        press = key.get_pressed() 
 
        if press[K_UP] and self.rect.y > 0: 
            self.rect.y -= self.speed 
        if press[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
        if press[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed 
        if press[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed 

class Enemy(GameSprite):
    direcktion = "right"

    def update(self):
        if self.rect.x <= 470:
            self.direcktion = "right"
        if self.rect.x >= win_width -80:
           self.direcktion = "left" 
        
        if self.direcktion == "left": 
            self.rect.x -= self.speed 
        if self.direcktion == "right": 
            self.rect.x += self.speed

class Wall(sprite.Sprite):  
    def __init__(self, color, wall_x, wall_y, wall_width, wall_hight ):
        super(). __init__()
        self.fill_color = color

        self.wight = wall_width
        self.hight = wall_hight

        self.image = Surface((self.wight, self.hight))
        self.image.fill(color)
        self.rect = self.image.get_rect()

        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_well(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#Ігрова сцена:  
win_width = 700  
win_height = 500  
  
  
window = display.set_mode((win_width, win_height))  
display.set_caption("Maze")  
background = transform.scale(image.load("background.jpg"), (win_width, win_height))  
   
#Персонажі гри:  
player = Player("hero.png", 100, 100, 10) 
player2 = Enemy("cyborg.png", 500, 200, 3) 
player3 = GameSprite("treasure.png", 510, 400, 10) 
  
 
#стіни 
wal1 = Wall((139, 91, 207), 65, 50, 10, 250)
wal2 = Wall((139, 91, 207), 65, 50, 150, 10)
wal3 = Wall((139, 91, 207), 210, 50, 10, 150)
wal4 = Wall((139, 91, 207), 65, 290, 150, 10)
wal5 = Wall((139, 91, 207), 210, 209, 150, 10)

game = True  
clock = time.Clock()  
FPS = 60  
  
  
#музика  
  
   
while game:  
    for e in event.get():  
        if e.type == QUIT:  
            game = False  
  
  
    window.blit(background,(0, 0))  
    player.update() 
    player.reset() 
    player2.update() 
    player2.reset() 
    player3.reset() 
    wal1.draw_well()
    wal2.draw_well()
    wal3.draw_well()
    wal4.draw_well()
    wal5.draw_well()

    display.update()  
    clock.tick(FPS)
