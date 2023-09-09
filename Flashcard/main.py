from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
global random_number, random_french_word

data = pandas.read_csv('./data/french_words.csv')
data_dict = data.to_dict()


def randomword():
    global random_number, flip_timer, random_french_word
    window.after_cancel(flip_timer)
    random_number = random.randrange(0, 100)
    random_french_word = data_dict['French'][random_number]
    canvas.itemconfig(french_title, text="French", fill="black")
    canvas.itemconfig(french_word, text=random_french_word, fill="black")
    canvas.itemconfig(canvas_img, image=card_front_img)
    flip_timer = window.after(3000, card_flip)


def card_flip():
    canvas.itemconfig(french_title, text="English", fill="white")
    canvas.itemconfig(canvas_img, image=card_back_img)
    random_english_word = data_dict['English'][random_number]
    canvas.itemconfig(french_word, text=random_english_word, fill="white")


window = Tk()
window.title("FlashCards")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = window.after(3000, card_flip)

canvas = Canvas(width=800, height=536)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
canvas_img = canvas.create_image(400, 263, image=card_front_img)
french_title = canvas.create_text(400, 163, text="French", font=('Arial', 40, 'italic'), fill="black")
french_word = canvas.create_text(400, 263, text="word", font=('Arial', 60, 'bold'), fill="black")
canvas.grid(column=0, row=0, columnspan=2)

wrong_button_img = PhotoImage(file='./images/wrong.png')
wrong_button = Button(image=wrong_button_img, highlightbackground=BACKGROUND_COLOR, command=randomword)
wrong_button.grid(column=0, row=1, pady=50)

right_button_img = PhotoImage(file='./images/right.png')
right_button = Button(image=right_button_img, highlightbackground=BACKGROUND_COLOR, command=randomword)
right_button.grid(column=1, row=1, pady=50)

randomword()

window.mainloop()
