import time
import tkinter as tk
from tkinter import font
import threading

root = tk.Tk()
root.title("Stopwatch")

# ---- Define globals ---

is_running = False 
start = 0
counter = tk.StringVar()
fontstyle = font.Font(size = 24)
score = 0
ntry = 0
score_display = tk.StringVar()
game_mode = tk.IntVar()


# ---- Define helper functions ----

def format_start(start):
    """Takes time in seconds with one decimal precision and 
    formats it to minute:second.milliseconds format"""
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
    """If the stopwatch is running, updates the time in 0.1 second
    interval and updates the label"""
    global start, counter
    while(is_running):
        counter.set(format_start(start))
        time.sleep(0.1)
        start += 0.1
        start = round(start, 1)

def timer_reset():
    """Event handler for reset button. Resets value of score and time.
    Updates labels for score and time."""
    global is_running, start, counter, ntry, score
    is_running = False
    start = ntry = score = 0
    counter.set(format_start(start))
    score_display.set(format_score())

def timer_stop():
    """Event handler for stop button. Updates score(number of times
    a player stops at exact second) and ntry(total number of times
    a player hits stop)."""
    global is_running, ntry, score
    is_running = False
    ntry += 1
    if int(start * 10) % 10 == 0:
        score += 1
    score_display.set(format_score())

def timer_start():
    """Event handler for start. Fires the timer function in a separate
    thread to avoid locking up the UI."""
    global is_running
    is_running = True
    x = threading.Thread(target = timer)
    x.start()

def toggle_game_mode():
    """Event handler for game mode checkbox. Hides the score label when
    turned off, calls the reset function each time it is toggled."""
    if game_mode.get() == 1:
        score_label.grid(row = 2, column = 2, sticky = tk.W)
    else:
        score_label.grid_forget()
    timer_reset()

# ---- GUI ----

start_button = tk.Button(root, text = "Start", command = timer_start,
        bg = "#127c34", fg = "#f7f6dc", font = fontstyle, width = 4)
start_button.grid(row = 0, column = 0, sticky = tk.W, pady = 10, padx = 5)

stop_button = tk.Button(root, text = "Stop", command = timer_stop,
        bg = "#961515", fg = "#f7f6dc", font = fontstyle, width = 4)
stop_button.grid(row = 0, column = 1, sticky = tk.W, pady = 10, padx = 5)

reset_button = tk.Button(root, text = "Reset", command = timer_reset,
        bg = "#1d3557", fg = "#f7f6dc", font = fontstyle, width = 4)
reset_button.grid(row = 0, column = 2, sticky = tk.W, pady = 10, padx = 5)

counter_label = tk.Label(root, textvariable = counter, fg = "#2c302e",
        font = ("default", 60), height = 1, width = 7)
counter_label.grid(row = 1, columnspan = 3, pady = 20)

score_label = tk.Label(root, textvariable = score_display, fg = "#2c302e",
        font = ("default", 16))

score_toggle = tk.Checkbutton(root, text = "Game Mode", variable = game_mode,
        command = toggle_game_mode, font = ("default", 14))
score_toggle.grid(row = 2, column = 0, columnspan = 2, sticky = tk.W, pady = 10
    )

timer_reset()

root.mainloop()
