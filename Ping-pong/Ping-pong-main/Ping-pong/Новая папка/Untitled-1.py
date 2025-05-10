
from pygame import *

window = display.set_mode((700, 500))
display.set_caption('Пинг-понг')
win_height = 500
win_wight = 700
background = transform.scale(image.load('zadniy_fon.jpg'), (win_wight, win_height))


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_hight, player_wight):
        super().__init__()
        self.hight = player_hight
        self.wight = player_wight
        self.image = transform.scale(image.load(player_image), (self.wight,self.hight))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_1(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 240:
            self.rect.y += self.speed

    def update_2(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 240:
            self.rect.y += self.speed


ball = GameSprite('ping_pong_ball.png', 350, 250, 3, 50, 50)
racket_1 = Player('ping_pong_racket.png', 50, 250, 5, 250, 25)
racket_2 = Player('ping_pong_racket.png', 650, 250, 5, 250, 25)

font.init()
font = font.Font(None, 70)


clock = time.Clock()
FPS = 60
game = True
finish = False
hit = 0

num_fire = 0
real_time = False
speed_x = 3
speed_y = 3
while game:
    window.blit(background,(0, 0))

    keys_pressed = key.get_pressed()
    
    if finish != True:

        racket_1.reset()
        racket_1.update_2()

        racket_2.reset()
        racket_2.update_1()

        ball.reset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            speed_y *= -1

        if sprite.collide_rect(racket_1, ball) or sprite.collide_rect(racket_2, ball):
            speed_x *= -1
        
        if ball.rect.x > win_wight - 50 or ball.rect.x < 0:
            win = font.render('YOU WIN!', True, (255, 215, 0))
            finish = True

    for e in event.get():
        if e.type == QUIT:
            game = False

    clock.tick(FPS)

    display.update()