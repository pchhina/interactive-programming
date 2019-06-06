import tkinter as tk
import random

root = tk.Tk()
root.title("Guess the Number")

# define globals
var = tk.StringVar()
result = tk.StringVar()
trials = tk.StringVar()

# ----Helper Functions----
def new_game():
    """Initializes global variables."""
    global ntry, actual
    actual = random.randint(1,100)
    ntry = 7
    msg = "You have {0} trials remaining".format(ntry)
    trials.set(msg)
    entry_question.config(state = 'normal')

def set_message(event):
    """Updates the message with new text in entry field."""
    guess = entry_question.get()
    msg = "Your guess is " + guess
    var.set(msg)


def check_guess(event):
    """Compares user's guess with actual number and updates the results
    message."""
    global ntry
    guess = int(entry_question.get())
    if guess > actual:
        result.set("Actual number is smaller")
    elif guess < actual:
        result.set("Actual number is larger")
    else:
        result.set("You guessed it correct!")
        trials.set("Please reset to play again")
        entry_question.config(state = 'disabled')
        return
    ntry -= 1
    in_play()
    
def in_play():
    """Check if the game is in play and sets the message and entry state."""
    if ntry < 1:
        msg = "Please reset to play again"
        trials.set(msg)
        result.set("")
        var.set("")
        entry_question.config(state = 'disabled')
        return False
    else:
        msg = "You have {0} trials remaining".format(ntry)
        trials.set(msg)
        return True


# ----UI----

label_title = tk.Label(root, text = "Guess the Number",
        font = ("", 16))
label_title.grid(row = 0, column = 0, columnspan = 2)

reset_button = tk.Button(root, text = "Reset", command = new_game,
        bg = "#009300", fg = "#e6e6e6")
reset_button.grid(row = 60, column = 0, sticky = tk.W,
        padx = 5, pady = 5)

quit_button = tk.Button(root, text = "Quit", command = root.destroy,
        bg = "#ff4848", fg = "#e6e6e6")
quit_button.grid(row = 60, column = 1, sticky = tk.E,
        padx = 5, pady = 5)


label_question = tk.Label(root, text = "Enter your guess")
label_question.grid(row = 10, column = 0, padx = 10, pady = 20)

entry_question = tk.Entry(root)
entry_question.focus_force()
entry_question.grid(row = 10, column = 1, padx = 10)

label_guess = tk.Label(root, textvariable = var)
label_guess.grid(row = 30, column = 0, pady = 5, columnspan = 2)

label_result = tk.Label(root, textvariable = result)
label_result.grid(row = 40, column = 0, pady = 5, columnspan = 2)

label_trials = tk.Label(root, textvariable = trials)
label_trials.grid(row = 50, column = 0, pady = 5, columnspan = 2)

# add = "+" adds the handler to handler list
# this allows multiple handlers to bind to single event
root.bind("<Return>", set_message, add = "+") 
root.bind("<Return>", check_guess, add = "+")

new_game()

root.mainloop()
