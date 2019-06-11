import time
import tkinter as tk
import threading

root = tk.Tk()
root.geometry("300x150")

# ---- Define globals ---
is_running = False 
start = 0


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
    global start
    while(is_running):
        time.sleep(0.1)
        print(format_start(start))
        start += 0.1
        start = round(start, 1)

def timer_reset():
    global is_running, start
    is_running = False
    start = 0

def timer_stop():
    global is_running
    is_running = False

def timer_start():
    global is_running
    is_running = True
    x = threading.Thread(target = timer)
    x.start()

# ---- GUI ----

start_button = tk.Button(root, text = "Start", command = timer_start)
start_button.grid(row = 0, column = 0)

stop_button = tk.Button(root, text = "Stop", command = timer_stop)
stop_button.grid(row = 0, column = 1)

reset_button = tk.Button(root, text = "Reset", command = timer_reset)
reset_button.grid(row = 0, column = 2)

root.mainloop()
