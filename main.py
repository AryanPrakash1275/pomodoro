import math
from tkinter import *
import time
# ------------------- Constants ---------------------

pink = "#e2979c"
red = "#e7305b"
green = "#9bdeac"
yellow = "#f7f5dd"
font_name = "Courier"
work_minutes = 25 * 60
break_minutes = 5 * 60
long_break_minutes = 20 * 60
reps = 0
timer_check = None
# ----------------------reset_mechanism------------


def reset_mechanism():
    window.after_cancel(timer_check)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0


# --------------time start--------------------


def timer_start():
    global reps
    reps += 1

    if reps % 8 == 0:
        timer(long_break_minutes)
        timer_label.config(text="Long Break", fg=red)
    elif reps % 2 == 0:
        timer(break_minutes)
        timer_label.config(text="Short Break", fg=pink)
    else:
        timer(work_minutes)
        timer_label.config(text="Work!", fg=green)

# --------------- time mechanism -------------


def timer(count):

    count_in_minute = math.floor(count/60)
    count_in_second = count % 60
    if count_in_second == 0:
        count_in_second = "00"
    elif count_in_second < 10:
        count_in_second = f"0{count_in_second}"

    canvas.itemconfig(timer_text, text=f"{count_in_minute}:{count_in_second}")
    if count > 0:
        global timer_check
        timer_check = window.after(1000, timer, count - 1)
    else:
        timer_start()
        tick_mark = ""
        for var in range(math.floor(reps/2)):
            tick_mark += "✔"
            check_marks.config(text=tick_mark)

# ---------------- GUI ------------------


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=yellow)
window.after(1000)

timer_label = Label(text="Timer", fg=green, font=(font_name, 50,), bg=yellow)
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=yellow, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(font_name, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, width=8, command=timer_start)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, width=8, command=reset_mechanism)
reset_button.grid(column=2, row=2)

check_marks = Label(text="✔", fg=green)
check_marks.grid(column=1, row=2)


window.mainloop()
