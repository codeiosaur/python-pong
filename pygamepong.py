import pygame as pg
import sys
import time
import random

# Change these to whatever you want
WIDTH = 800; HEIGHT = 800
pg.init()
clock = pg.time.Clock()
paddleX = 100
paddleY = 225
BALL_RADIUS = 20
BALL_COLOR = (255,255,255)

# Colours
BACKGROUND = (0,0,0)

class Ball:
    def __init__(self,surface,color):
        pg.sprite.Sprite.__init__(self)
        self.x = WIDTH // 2 ; self.y = HEIGHT // 2 # coordinate init
        self.color = color
        self.image = pg.Surface((BALL_RADIUS,BALL_RADIUS)); self.image.set_alpha((0)); self.image.fill((0,0,0)) # image init
        pg.draw.circle(self.image,self.color,(self.x,self.y),BALL_RADIUS,0)
        pg.display.flip()

        self.momentumX = random.choice((-1,1))
        self.momentumY = random.choice((-1,1))

class Paddle:
    def __init__(self,surface,color):
        pg.sprite.Sprite.__init__(self)
        self.y = 225
        self.color = color
        self.image = pg.Surface((30,375))
        self.image.fill((255,255,255))
        pg.display.flip()

    def up(self):
        self.y -= 1

    def down(self):
        self.y += 1

root = pg.display.set_mode((WIDTH,HEIGHT),pg.SCALED)
pg.display.set_caption('Pong')

background = pg.Surface(root.get_size())
background = background.convert()
background.fill((0,0,0))
root.blit(background, (0,0))
pg.display.flip()


paddle = Paddle(root,(255,255,255))
ball = Ball(root,BALL_COLOR)

going = True



while going:
    # -- event handling -- #
    for event in pg.event.get():
        if event.type == pg.QUIT:
            going = False
            pg.quit(); sys.exit(0)
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                going = False
                pg.quit(); sys.exit(0)
    
    keys = pg.key.get_pressed()
    if keys[pg.K_s] and (paddle.y + 375) < HEIGHT and going == True:
        paddle.down()
    if keys[pg.K_w] and paddle.y > 0 and going == True:
        paddle.up()

    # --- ball handling/collisions --- #
    ball.x += ball.momentumX
    ball.y += ball.momentumY

    if (ball.x - BALL_RADIUS) > 0:
        if (ball.x + BALL_RADIUS) > WIDTH: # Hit the left/right edges respectively
            if ball.momentumX > 0:
                ball.momentumX += 1
            else:
                ball.momentumX -= 1
            ball.momentumX *= -1

        if ball.y < BALL_RADIUS or (ball.y + BALL_RADIUS) > HEIGHT: # Hit the top/bottom respectively
            if ball.momentumY > 0:
                ball.momentumY += 1
            else:
                ball.momentumY -= 1
            ball.momentumY *= -1
    else: # The ball hit the left screen edge
        going = False
        time.sleep(0.5)
        break

    # --- ball/paddle collisions --- # 
    if ball.x <= 100 + 30 and ball.x > 100: # Did the ball hit the paddle on the x side?
        if paddle.y < ball.y and paddle.y + 375 > ball.y:
            ball.momentumX *= -1

    # --- rendering --- #
    root.fill(BACKGROUND)
    root.blit(paddle.image,(paddleX,paddle.y))
    #root.blit(ball.image,(ball.x,ball.y))
    pg.draw.circle(root,BALL_COLOR,(ball.x,ball.y),BALL_RADIUS) # No idea why I need to draw again here (the ball)

    # --- updates --- #
    pg.display.update()
    clock.tick(100)


pg.quit()