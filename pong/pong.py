import tkinter as tk
import time

root = tk.Tk()
root.title("Pong")

# First foray into classes
class Pong:
    def __init__(self, master):
        self.width = 1000
        self.height = 800
        self.window = tk.Canvas(master, width = self.width, height = self.height)
        self.window.grid()
        self.paddlewidth = 20
        self.paddleheight = 100
        self.left_padpos = 0
        self.right_padpos = 980

        # draw paddles
        self.left_paddle = self.window.create_rectangle(self.left_padpos,
                self.left_padpos,
                self.left_padpos + self.paddlewidth,
                self.left_padpos + self.paddleheight,
                fill = "red")
        self.right_paddle = self.window.create_rectangle(self.right_padpos,
                0,
                self.right_padpos + self.paddlewidth,
                self.paddleheight,
                fill = "blue")


        # draw ball at the center of the canvas
        center = [self.width / 2, self.height / 2]
        radius = 50
        x0 = center[0] - radius
        y0 = center[1] - radius
        x1 = center[0] + radius
        y1 = center[1] + radius
        self.ball = self.window.create_oval(x0, y0, x1, y1)

        # initialize velocity
        self.v = [1, 1]

        
    def velocity(self, pos):
        if pos[2] > self.width or pos[0] < 0:
            self.v[0] *= -1
        if pos[3] > self.height or pos[1] < 0:
            self.v[1] *= -1
        return self.v

    def move_ball(self):
        while True:
            pos = self.window.coords(self.ball)
            ball_speed = self.velocity(pos)
            self.window.move(self.ball, ball_speed[0], ball_speed[1])
            time.sleep(0.02)
            root.update()

    def move_paddle(self, event):
        pos_left = self.window.coords(self.left_paddle)
        pos_right = self.window.coords(self.right_paddle)
        if event.char == "f" and pos_left[3] < self.height:
            self.window.move(self.left_paddle, 0, 10)
        if event.char == "d" and pos_left[1] > 0:
            self.window.move(self.left_paddle, 0, -10)
        if event.char == "j" and pos_right[3] < self.height:
            self.window.move(self.right_paddle, 0, 10)
        if event.char == "k" and pos_right[1] > 0:
            self.window.move(self.right_paddle, 0, -10)
            root.update()

pong = Pong(root)
root.bind("<Key>", pong.move_paddle)
pong.move_ball()
