import time
import tkinter as tk
from tkinter import font
import threading

root = tk.Tk()
root.geometry("450x350")
root.title("Stopwatch")

# ---- Define globals ---
is_running = False 
start = 0
counter = tk.StringVar()
fontstyle = font.Font(size = 24)


# ---- Define helper functions ----
def format_start(start):
    tenth_of_seconds = int(start * 10)
    minutes = tenth_of_seconds // 600
    tenth_of_seconds = tenth_of_seconds % 600
    if tenth_of_seconds < 100:
        tens_place = 0
    else:
        tens_place = ""
    seconds = tenth_of_seconds / 10
    formatted_time = "{0}:{1}{2}".format(minutes, tens_place, seconds)
    return formatted_time
    

def timer():
    global start, counter
    while(is_running):
        counter.set(format_start(start))
        time.sleep(0.1)
        start += 0.1
        start = round(start, 1)

def timer_reset():
    global is_running, start, counter
    is_running = False
    start = 0
    counter.set(format_start(start))

def timer_stop():
    global is_running
    is_running = False

def timer_start():
    global is_running
    is_running = True
    x = threading.Thread(target = timer)
    x.start()

# ---- GUI ----

start_button = tk.Button(root, text = "Start", command = timer_start,
        bg = "#127c34", fg = "#f7f6dc", font = fontstyle)
start_button.grid(row = 0, column = 0, pady = 25)

stop_button = tk.Button(root, text = "Stop", command = timer_stop,
        bg = "#961515", fg = "#f7f6dc", font = fontstyle)
stop_button.grid(row = 0, column = 1, pady = 25)

reset_button = tk.Button(root, text = "Reset", command = timer_reset,
        bg = "#1d3557", fg = "#f7f6dc", font = fontstyle)
reset_button.grid(row = 0, column = 2, pady = 25)

counter_label = tk.Label(root, textvariable = counter, bg = "#2c302e",
        fg = "#f7f6dc", font = ("default", 60), height = 2, width = 8)
counter_label.grid(row = 1, columnspan = 3, pady = 20, padx = 20)

timer_reset()

root.mainloop()
