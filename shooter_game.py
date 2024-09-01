from typing import Any
from pygame import *
from random import randint

mixer.init()
mixer.music.load("space.ogg")
mixer.music.play
fire_sound = mixer.Sound("fire.ogg")

font.init()
font1 = font.Font(None, 50)
font2 = font.Font(None, 36)
win = font1.render("Перемога", True, (255, 255, 255))
lose = font2.render("Програв", False, (150, 0, 0))

score = 0
lost = 0
max_lost = 3

goal = 41
life = 3

class GameSprite(sprite.Sprite):
    
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # викликаємо конструктор класу (Sprite):
        sprite.Sprite.__init__(self)
        # кожен спрайт повинен зберігати властивість image - зображення
        self.image = transform.scale(
            image.load(player_image), (size_x, size_y))
        self.speed = player_speed
 
        # кожен спрайт повинен зберігати властивість rect - прямокутник, в який він вписаний
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
    # метод, що малює героя на вікні
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

# клас головного гравця
class Player(GameSprite):
    
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_d] and self.rect.y < win_helght - 80:
            self.rect.y += self.speed

    def fire (self):
        bullet = Bullet(img_bullet, self.rect.centerx, self.rect.centery, 15, 30, -15)
        bullets.add(bullet)

class Enemy(GameSprite):
    def update(self):
        global lost
        self.rect.x -= self.speed
        if self.rect.x < 0:
            self.rect.y = randint(50, win_width + 50)
            self.rect.x = win_width
            lost += 1


class Bullet(GameSprite):
    def update(self):
        self.rect.x -= self.speed
        

img_back = "000.png"
img_hero = "rockets__2_-removebg-preview.png"
img_enemy = "8892.png_1200-removebg-preview.png"
img_bullet = "png-klev-club-pn0e-p-pikselnaya-pulya-png-4-removebg-preview.png"


win_width = 700
win_helght = 500
display.set_caption("Shooter")
window = display.set_mode((win_width, win_helght))
backdround = transform.scale(image.load(img_back), (win_width, win_helght))


ship = Player(img_hero, 0, 100, 80, 100, 40)

monsters = sprite.Group()
for i in range(1,6):
    monster = Enemy(img_enemy, win_width, randint(80, win_helght - 80), 80, 80, randint(1, 3))
    monsters.add(monster)

bullets = sprite.Group()

run = True

finish = False

while run:

    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                ship.fire()
            if e.key == K_1:
                ship.image = transform.scale(image.load(img_enemy), (80, 50))
            if e.key == K_2:
                ship.image = transform.scale(image.load(img_hero), (80, 100))


    if not finish:
        window.fill((0, 0, 0))
        window.blit(backdround, (0,0))

        text = font2.render("Рахунок: " + str(score), 1, (204, 255, 255))
        window.blit(text, (100, 100))

        text = font2.render("Пропущено: " + str(lost), 1, (204, 255, 255))
        window.blit(text, (100, 150))

        ship.update()
        monsters.update()
        bullets.update()

        collides = sprite.groupcollide(monsters, bullets, True, True)
        for c in collides:
            score = score + 1
            monster = Enemy(img_enemy, win_width, randint(80, win_helght - 80), 80, 80, randint(1, 3))
            monsters.add(monster)

        if sprite.spritecollide(ship, monsters, False):
            sprite.spritecollide(ship, monsters, True)
            life -= 1

        if life == 0 or lost >= max_lost:
            Finish = True
            window.blit(win, (200, 200))

        if score >= goal:
            finish = True
            window.blit(win, (200, 200))

        ship.reset()
        monsters.draw(window)
        bullets.draw(window)

        text_life = font1.render(str(life), 1, (200, 0, 0))
        window.blit(text_life, (650, 10))

        display.update()

    time.delay(50)