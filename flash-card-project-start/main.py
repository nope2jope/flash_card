from tkinter import *
import pandas
import random
import time

BACKGROUND_COLOR = "#B1DDC6"

# randomize words with pandas

dictionary = pandas.read_csv('./data/french_words.csv')
new_frame = dictionary.to_dict(orient='index')

learned = []

# retrieve CSV




def randomize_word():
    randy = random.choice(new_frame)
    fr = randy["French"]
    eng = randy["English"]
    pair = [fr, eng]
    return pair

def flip_that():
    global word_pair
    word_pair = randomize_word()
    fr = word_pair[0]
    eng = word_pair[1]

    canvas.itemconfig(canvas_image, image=card_front)
    canvas.itemconfig(lang_label, text = "f r e n c h", fill='black')
    canvas.itemconfig(word_label, text=fr, fill='black')
    window.update()
    window.after(3000)
    window.update()
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(lang_label, text= "e n g l i s h", fill='white')
    canvas.itemconfig(word_label, text=eng, fill='white')

def got_it():
    new_frame.remove(word_pair)
    to_learn = pandas.DataFrame(new_frame)
    to_learn.to_csv("./data/to_learn.csv")
    flip_that()

# initialize window

window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("f l a s h t h i s")

# set card images

card_front = PhotoImage(file='./images/card_front.png')
card_back = PhotoImage(file='./images/card_back.png')
check_mark = PhotoImage(file='./images/right.png')
ex_mark = PhotoImage(file='./images/wrong.png')

# initialize canvas

canvas = Canvas(height=525, width=800)
canvas_image = canvas.create_image(400, 263, image=card_front)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# initialize labels

lang_label = canvas.create_text(400, 150, text="T I T L E", font=("Arial", 20, 'italic'))

word_label = canvas.create_text(400, 225, text="W O R D", font=('Arial', 30, 'bold'))

# initialize buttons

check_button = Button(image=check_mark, highlightthickness=0, command=got_it)
check_button.grid(row=1, column=0)

wrong_button = Button(image=ex_mark, highlightthickness=0, command=flip_that)
wrong_button.grid(row=1, column=1)

# run window



window.mainloop()