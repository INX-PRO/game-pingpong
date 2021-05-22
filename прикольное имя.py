from pygame import *
from random import*
#font.init()



class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(wight, height))
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
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed


r = Player("r2.1.png",9,5,5,75,75)
rr = Player("rr.png",5,250,5,50,150)
rrr = Player("rrr.png",546,250,5,50,150)


back = (200,255,255)
win_width = 600
win_height = 500
window =  display.set_mode((win_width,win_height))
window.fill(back)
#display.set_caption("пинпонг")
#background = transform.scale(image.load('galaxy.jpg'),(700,500))

#sprite1 = transform.scale(image.load('l.png'),(100,100))
clock = time.Clock()
FPS = 120
game = True

speed_x = 3
speed_y = 3

game = True
Finish = False
font = font.SysFont(None,50)
win = font.render('YOU WIN',True,(255,215,0))
los = font.render('YOU LOSE',True,(255,0,0))

while game:
    
    for e in event.get():
        if e.type == QUIT:
            game = False 

    window.fill(back)
    r.rect.x += speed_x
    r.rect.y += speed_y

    if r.rect.y > 470 or  r.rect.y < 0:
        speed_y *= -1      



    if sprite.collide_rect(rr, r) or sprite.collide_rect(rrr, r):
        speed_x *= -1
        #score += 1

    """if Finish != True:
        
        if ball.rect.x < 0:
            window.blit(win2,(290,230))

        elif ball.rect.x > 700:
            window.blit"""

    r.update()
    r.reset()
    rr.update_l()
    rr.reset()
    rrr.update_r()
    rrr.reset()

    clock.tick(FPS)
    display.update()
