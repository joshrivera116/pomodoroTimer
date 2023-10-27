from tkinter import *
import pygame
import math
pygame.mixer.init()

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps, timer
    window.after_cancel(timer)
    reps = 0
    checkmark.config(text='')
    label.config(text='Timer')
    canvas.itemconfig(timer_text, text='00:00')


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        label.config(text='Work!', fg=GREEN)
        count_down(work_sec)

    elif reps == 2 or reps == 4 or reps == 6:
        label.config(text='Break!', fg=PINK)
        count_down(short_break)

    elif reps == 8:
        label.config(text='Break!', fg=RED)
        count_down(long_break)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    minutes = math.floor(count / 60)
    if minutes < 10:
        minutes = f'0{math.floor(count / 60)}'

    sec = count % 60
    if sec < 10:
        sec = f'0{sec}'
    canvas.itemconfig(timer_text, text=f'{minutes}:{sec}')
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
        if count < 5:
            sound = pygame.mixer.Sound('C:/Users/joshr/Downloads/alarm.mp3')
            sound.play(loops=0)
    else:
        start_timer()
        checks = ''
        sessions = math.floor(reps / 2)
        for i in range(sessions):
            checks += '✔'
        checkmark.config(text=checks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.minsize(450, 400)
window.config(padx=100, pady=50, bg=YELLOW)

window.after(1000, )

label = Label(text='Timer', font=(FONT_NAME, 40), bg=YELLOW, fg=GREEN)
label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file='tomato.png')

canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text='00:00', font=(FONT_NAME, 20))
canvas.grid(row=1, column=1)

checkmark = Label(bg=YELLOW, fg=GREEN, font=('Arial', 18))
checkmark.grid(row=3, column=1)

start_button = Button(text='Start', highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text='Reset', highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

window.mainloop()
