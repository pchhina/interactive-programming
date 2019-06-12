import time
import tkinter as tk
from tkinter import font
import threading

root = tk.Tk()
root.geometry("450x400")
root.title("Stopwatch")

# ---- Define globals ---
is_running = False 
start = 0
counter = tk.StringVar()
fontstyle = font.Font(size = 24)
score = 0
ntry = 0
score_display = tk.StringVar()


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
    
def format_score():
    score_disp = f"Score: {score}/{ntry}"
    return score_disp

def timer():
    global start, counter
    while(is_running):
        counter.set(format_start(start))
        time.sleep(0.1)
        start += 0.1
        start = round(start, 1)

def timer_reset():
    global is_running, start, counter, ntry, score
    is_running = False
    start = ntry = score = 0
    counter.set(format_start(start))
    score_display.set(format_score())

def timer_stop():
    global is_running, ntry, score
    is_running = False
    ntry += 1
    if int(start * 10) % 10 == 0:
        score += 1
    score_display.set(format_score())

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

score_label = tk.Label(root, textvariable = score_display, fg = "#2c302e",
        font = ("default", 20))
score_label.grid(row = 2, column = 2, pady = 10, padx = 10)

timer_reset()

root.mainloop()
