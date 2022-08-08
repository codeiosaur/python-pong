from tkinter import *
from tkinter.ttk import *
import time
import random

# Globals
SCREEN_WIDTH = 1000; SCREEN_HEIGHT = 1000
BALL_RADIUS = 10
PADDLE_LEN = 100; PADDLE_WIDTH = 10


class Ball:
    def __init__(self,canvas,centerX,centerY,color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval((centerX-(25/2)),(centerY-(25/2)),(centerX+(25/2)),(centerY+(25/2)),fill=color)
        self.x = 3; self.y = random.randint(-3,3)
        self.hit_bottom = False
    
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0 or pos[3] >= SCREEN_HEIGHT:
            self.y *= -1
        if pos[2] >= SCREEN_WIDTH:
            self.x *= -1
        if self.hit_paddle(pos) == True:
            self.x = 3
            self.y += random.randint(-2,2)
        if pos[0] <= 0:
            self.hit_bottom = True

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] > paddle_pos[0] and pos[0] < paddle_pos[2]:
            if pos[3] > paddle_pos[1] and pos[1] < paddle_pos[3]:
                return True
        return False

class Paddle:
    def __init__(self, canvas, cornerX, cornerY, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(cornerX,cornerY,cornerX+20,cornerY+200,fill=color)
        self.x = 0; self.y = 0
        game.bind_all('<Up>',self.paddle_up)
        game.bind_all('<Down>',self.paddle_down)

    def draw(self):
        self.canvas.move(self.id,0,self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0 or pos[3] >= SCREEN_HEIGHT:
            self.y = 0

    def paddle_up(self,event):
        self.y = -2
    
    def paddle_down(self,event):
        self.y = 2


game = Tk()
game.title('Pong'); game.geometry(f'{SCREEN_WIDTH}x{SCREEN_HEIGHT}')
game.resizable(height=False,width=False); game.wm_attributes('-topmost', 1)

canvas = Canvas(game, width=SCREEN_WIDTH, height=SCREEN_HEIGHT, bd=0, bg='black',highlightthickness=0)
canvas.pack()
game.update()

paddle = Paddle(canvas,100,400,'white')
ball = Ball(canvas,500,100,'white')
#game_over = Label(canvas,text='GAME OVER',font=('Helvetica',20))
#game_over.pack()
game.update()

while True: # mainloop
    if ball.hit_bottom == False:
        ball.draw()
        paddle.draw()
    game.update_idletasks()
    game.update()
    time.sleep(0.01)
