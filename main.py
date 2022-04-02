from tkinter import  *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def resets():
    window.after_cancel(timer)
    canvas.itemconfig(text_can, text="00:00")
    label.config(text="Timer",fg=GREEN)
    label_2.config(text="")
    global REPS
    REPS=0






# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_count():
    global REPS
    REPS += 1

    work_reps = WORK_MIN * 60
    break_reps = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60


    if REPS % 8 == 0:
        count_down(long_break)
        label.config(text="Break", fg=RED, bg=YELLOW)
    elif REPS % 2 == 0:
         count_down(break_reps)
         label.config(text="Break", fg=PINK, bg=YELLOW)
    else:
        count_down(work_reps)
        label.config(text="Work", fg=GREEN, bg=YELLOW)




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(text_can, text = f"{count_min}:{count_sec}")
    if count > 0:

       timer = window.after(1000, count_down, count - 1)
    else:
        start_count()
        marks = ""
        for _ in range(math.floor(REPS/2)):
            marks += "✔"
        label_2.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas =Canvas(width=200,height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100 ,104,image=tomato)
text_can = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME,34,"bold"))
canvas.grid(column=2,row=2)

label = Label(bg=YELLOW)
label.config(text="Timer", fg=GREEN , font=(FONT_NAME,35, "bold"))
label.grid(column=2,row=1)
# text="✔",
label_2 = Label(bg=YELLOW)
label_2.config( fg=GREEN , font=(FONT_NAME,15, "bold"))
label_2.grid(column=2,row=3)

button = Button(text="Start",command=start_count)
button.grid(column=1,row=3)

button= Button(text="Reset",command=resets)
button.grid(column=3,row=3)


window.mainloop()