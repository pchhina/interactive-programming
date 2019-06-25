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

        # draw ball at the center of the canvas
        center = [self.width / 2, self.height / 2]
        radius = 50
        x0 = center[0] - radius
        y0 = center[1] - radius
        x1 = center[0] + radius
        y1 = center[1] + radius
        self.ball = self.window.create_oval(x0, y0, x1, y1)

        # initialize velocity
        self.v = 10
        
    def velocity(self, pos):
        if pos[2] > self.width or pos[0] < 0:
            self.v *= -1
        return self.v

    def move_ball(self):
        while True:
            pos = self.window.coords(self.ball)
            self.window.move(self.ball, self.velocity(pos), 0)
            time.sleep(0.02)
            root.update()

pong = Pong(root)

pong.move_ball()
