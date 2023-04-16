from tkinter import *
import pandas
import random
import os

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")

else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer, to_learn
    if len(to_learn) == 0:
        os.remove("data/words_to_learn.csv")
        reverted_data = pandas.read_csv("data/french_words.csv")
        to_learn = reverted_data.to_dict(orient="records")
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(view_image, image=card_front_img)
    canvas.itemconfig(card_title, text="- - French - -", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    flip_timer = window.after(4000, func=flip_card)


def is_known():
    to_learn.remove(current_card)
    unknown_words = pandas.DataFrame(to_learn)
    unknown_words.to_csv("data/words_to_learn.csv", index=False)

    next_card()


def flip_card():
    canvas.itemconfig(view_image, image=card_back_img)
    canvas.itemconfig(card_title, text="- - English - -", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


window = Tk()
window.title("Flash - Study")
window.config(width=900, height=700, padx=100, pady=100, bg=BACKGROUND_COLOR, highlightthickness=0)

flip_timer = window.after(4000, func=flip_card)

canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
card_back_img = PhotoImage(file="images/card_back.png")
card_front_img = PhotoImage(file="images/card_front.png")
view_image = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 100, font=("verdana", 30, "bold"))
card_word = canvas.create_text(400, 300, font=("verdana", 50, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown = Button(image=cross_image, pady=50, highlightthickness=0, command=next_card)
unknown.config(pady=50)
unknown.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known = Button(image=check_image, pady=50, highlightthickness=0, command=is_known)
known.config(pady=50)
known.grid(row=1, column=1)

next_card()
window.mainloop()
