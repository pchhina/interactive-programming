import tkinter as tk
import time

root = tk.Tk()
root.title("Pong")

# First foray into classes
class Paddle:
    """paddle for the pong game"""
    WIDTH = 20
    HEIGHT = 90

    def __init__(self, canvas, x0, y0, color):
        self.paddle = canvas.create_rectangle(x0, y0, x0 + Paddle.WIDTH,
                y0 + Paddle.HEIGHT, fill = color)

class Pong:
    def __init__(self, master):
        self.width = 1000
        self.height = 800
        self.window = tk.Canvas(master, width = self.width, height = self.height)
        self.window.grid()

        # draw paddles
        left_paddle = Paddle(self.window, 0, 0, "red")
        right_paddle = Paddle(self.window, self.width - Paddle.WIDTH, 0, "blue")

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
        print(self.v)
        return self.v

    def move_ball(self):
        while True:
            pos = self.window.coords(self.ball)
            ball_speed = self.velocity(pos)
            self.window.move(self.ball, ball_speed[0], ball_speed[1])
            print(pos)
            time.sleep(0.02)
            root.update()

pong = Pong(root)

pong.move_ball()
