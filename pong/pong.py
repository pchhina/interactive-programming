import tkinter as tk
import time

root = tk.Tk()
root.title("Pong")

class Pong:
    """Represents the game of pong.

    """
    def __init__(self, master):
        self.width = 1000
        self.height = 800
        self.window = tk.Canvas(master, width = self.width, height = self.height)
        self.window.grid()
        self.paddlewidth = 20
        self.paddleheight = 150
        self.left_padpos = 0
        self.right_padpos = 980
        self.v = [1, 1] # initial ball velocity
        self.left_score = 0
        self.right_score = 0

        # draw gutters
        self.window.create_line(20, 0, 20, 800, fill = "#8F8E8F")
        self.window.create_line(980, 0, 980, 800, fill = "#8F8E8F")

        # draw paddles
        self.left_paddle = self.window.create_rectangle(self.left_padpos,
                self.left_padpos,
                self.left_padpos + self.paddlewidth,
                self.left_padpos + self.paddleheight,
                fill = "#CBAB27")
        self.right_paddle = self.window.create_rectangle(self.right_padpos,
                0,
                self.right_padpos + self.paddlewidth,
                self.paddleheight,
                fill = "#209178")

        # score labels
        self.left_score_label = self.window.create_text(400, 50, 
                font = ("default", 60), fill = "#8f8e8f",
                text = self.left_score)
        self.right_score_label = self.window.create_text(600, 50, 
                font = ("default", 60), fill = "#8f8e8f",
                text = self.right_score)
    


        # draw ball at the center of the canvas
    def spawn_ball(self):
        self.v = [1, 1] # initial ball velocity
        center = [self.width / 2, self.height / 2]
        radius = 50
        x0 = center[0] - radius
        y0 = center[1] - radius
        x1 = center[0] + radius
        y1 = center[1] + radius
        self.ball = self.window.create_oval(x0, y0, x1, y1, fill = "#D73E44",
                outline = "#9D2E3E")

    def velocity(self, pos):
        pos_left = self.window.coords(self.left_paddle)
        pos_right = self.window.coords(self.right_paddle)
        pos_ballcenter = (pos[1] + pos[3]) / 2
        if pos[2] > self.width - self.paddlewidth:
            if pos_right[1] < pos_ballcenter < pos_right[3]:
                self.v[0] *= -1.1
            else:
                self.window.delete(self.ball)
                self.spawn_ball()
                self.left_score += 1
        if pos[0] < self.paddlewidth:
            if pos_left[1] < pos_ballcenter < pos_left[3]:
                self.v[0] *= -1.1
            else:
                self.window.delete(self.ball)
                self.spawn_ball()
                self.right_score += 1

        if pos[3] > self.height or pos[1] < 0:
            self.v[1] *= -1
        return self.v

    def move_ball(self):
        while True:
            pos = self.window.coords(self.ball)
            ball_speed = self.velocity(pos)
            self.window.move(self.ball, ball_speed[0], ball_speed[1])
            self.window.itemconfigure(self.left_score_label, text =
                    self.left_score)
            self.window.itemconfigure(self.right_score_label, text =
                    self.right_score)
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
pong.spawn_ball()
pong.move_ball()
