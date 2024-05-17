from pygame import *
from random import randint
from time import time as timer



font.init()
font! = font.Font(None, 80)
win = font1.render('You Win', True, (0,250,0))
lose = font1.render('Game Over', True, (250,0,0))

font2 = font.Font(None, 36)

ъхscore = 0
lost = 0
max_lost = 10
life = 3

img_bullet = 'bullet.png'

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_y, size_x))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def rect (self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_Width - 5:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet(img_bullet, self.rect,center, self.rect.top, 10,20, -10)
        bullets.add(bullet)

class Enemy(GameSprite):
    def update(self):
        if self.rect.y < win_height:
            self.rect.y += self.speed
            global lost
        else:
            self.rect.y = -100
            self.rect.x = randint(80, win_Width-80)
            lost += 40

class Meteor(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y < win_height:
            self.rect.x = randint(80, win_Width-80)
            lost += 40


class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed:
        if self.rect.y < 0:
            self.kill()

win_Width = 700
win_height = 500
player = Player('rocket.png', 5, win_height - 105, 80, 100, 10)

monsters = sprite.Group()
for i in range(5):
    monsters = Enemy('ufo.png', randint(80, win_Width - 80), -40, 80,40, randint(1,5))
    monsters.add(monsters)

Meteor = sprite.Group()
for i in range(2):
    Meteor = Enemy('asteroid.png', randint(80, win_Width - 80), -40, 80,40, randint(1,5))
    Meteor.add(Meteor)


bullets = sprite.Group()


game = True
finish = False
clock = time.Clock()
FPS = 60

mixer.init()
mixer.music.load('')
mixer.musik.play()
run_time = False
num_fire = 0

while game:
    for e in event.get():
        if e.type == QUIT:
            run = False
        if e.type == KEYDOWN:
            if e.type ==K_SPACE:
                if num_fire < 5 and rel_time == False:
                    num_fire += 1
                    ship.fire()

                if num_fire > 5 and rel_time == False:
                    num_time = timer()
                    rel_time = True

    if not finish:
        window.blit(background,(0,0))

        text_score =font2.render('Счет: ' + str(score), True, (255,0,0))
        window.blit(text_score,(10,20))

        text_lost =font2.render('Пропущено: ' + str(lost), True, (255,0,0))
        window.blit(text_lost,(10,50))

        if lost > max_lost or sprite.spritecollide(player,monsters, False):
            window.blit(lose,(300, win_height // 2))
            display.flip()
            finish = True

        collides = sprite.groupcollide(monsters, bullets, True, True)
        for c in collides:
            score += 1
            monster = Enemy('ufo.png', randint(80, win_Width - 80),-40, 80, 40, randint(1,5))
            monsters.add(monster)


        if core == 10:
            window.blit(win,(300, win_height // 2))
            display.flip()
            finish = True



        player.rect()
        player.speed()
        
        monsters.draw(window)
        monsters.update()

        Meteor.draw(window)
        Meteor.update()

        bullet.draw(window)
        bullet.update()

        display.update()

        if rel_time == True:
            now = timer()

            if now - lasttime < 3:
                reload = front2.render('Wait, roload.....', True,(255,0,0))
                window.blit(reload, (260, 460))
            else:
                num_fire = 0
                rel_time = False

        if sprite.spritecollide(ship, monsters, True):
            monster = Enemy('ufo.png', randint(80, win_Width - 80),-40, 80, 40, randint(1,5))
            monsters.add(monster)
            life -= 1
        if sprite.spritecollide(ship, monsters, True):
            monster = Meteor('asteroid.png', randint(80, win_Width - 80),-40, 80, 40, randint(1,5))
            monsters.add(monster)
            life -= 1

        if life == 3:
            ife_color = (0, 250, 0)
        if life == 2:
            life_color = (0, 250, 250)
        if life == 1:
            life_color = (200, 0, 0)
        if life == 0:
            life_color = (255, 0, 0)

        text_life = front1.render(srt(life), True, life_color)
        window.blit(text_life,(650, 10))
        display.update()

        if score == 10:
            window.blit(lose,(200, win_height // 2))
            display.flip()
            finish = True

        if score == 10:
            window.blit(win,(200, win_height // 2))
            display.flip()
            finish = True

    #clock.tick(FPS)
    time.delay(50)