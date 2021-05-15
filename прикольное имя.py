from pygame import *
from random import*
#font.init()

r = Player("r.png",299,435,5)
rr = Player("rr.png",299,435,5)
rrr = Player("rrr.png",299,435,5)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y


    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y)) 


class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()

        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_r(self):
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed


back = (200,255,255)
win_width = 600
win_hight = 500
window =  display.set_mode((win_width,win_hight))
window.fill(back)
#display.set_caption("пинпонг")
#background = transform.scale(image.load('galaxy.jpg'),(700,500))

#sprite1 = transform.scale(image.load('l.png'),(100,100))
clock = time.Clock()
FPS = 120
game = True



while game:
    
    for e in event.get():
        if e.type == QUIT:
            game = False        



    clock.tick(FPS)
    display.update()