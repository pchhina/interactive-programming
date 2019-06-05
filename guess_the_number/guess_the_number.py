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
    ntry -= 1
    in_play()
    
def in_play():
    """Check if the game is in play and sets the message and entry state."""
    if ntry < 1:
        msg = "Please reset to play again"
        trials.set(msg)
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

label_question = tk.Label(root, text = "Enter your guess")
label_question.grid(row = 1, column = 0, padx = 10, pady = 20)

entry_question = tk.Entry(root)
entry_question.grid(row = 1, column = 1, padx = 10)

label_guess = tk.Label(root, textvariable = var)
label_guess.grid(row = 3, column = 0, pady = 5, columnspan = 2)

label_result = tk.Label(root, textvariable = result)
label_result.grid(row = 4, column = 0, pady = 5, columnspan = 2)

label_trials = tk.Label(root, textvariable = trials)
label_trials.grid(row = 5, column = 0, pady = 5, columnspan = 2)

# add = "+" adds the handler to handler list
# this allows multiple handlers to bind to single event
root.bind("<Return>", set_message, add = "+") 
root.bind("<Return>", check_guess, add = "+")

new_game()

root.mainloop()
