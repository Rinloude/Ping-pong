
from pygame import *

window = display.set_mode((700, 500))
display.set_caption('Пинг-понг')
background = transform.scale((106, 90, 205), (700, 500))


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_hight, player_wight):
        super().__init__()
        self.hight = player_hight
        self.wight = player_wight
        self.image = transform.scale(image.load(player_image), (self.hight,self.wight))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#создание класса 
class Player(GameSprite):
    def update_1(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_UP] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_DOWN] and self.rect.x < 640:
            self.rect.x += self.speed


clock = time.Clock()
FPS = 60
game = True
finish = False
hit = 0

num_fire = 0
real_time = False
while game:
    window.blit(background,(0, 0))

    keys_pressed = key.get_pressed()
    
    for e in event.get():
        if e.type == QUIT:
            game = False

    clock.tick(FPS)

    display.update()