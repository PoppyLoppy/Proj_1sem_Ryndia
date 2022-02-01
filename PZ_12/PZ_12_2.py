# Вариант 21.
# Составить функцию, которая выполнит суммирование числового ряда.

from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Суммирование числового ряда")
root.geometry("300x150")


def close():
    root.destroy()
    root.quit


def rab():
    s = 0
    i = 1
    n = int(txt1.get())
    while i <= n:
        s += i
        i += 1
    str(s)
    rez = Label(text=s, width=9, font=("Times New Roman", 14), bg="#ffe3db")
    rez.grid(row=5, column=0, sticky=W+E, pady=5,  columnspan=3)


lab0 = Label(text="Введите последнее число ряда", font=("Times New Roman", 14), bg="#ffe3db", width=30)
lab0.grid(row=0, column=0, sticky=W+E, pady=5,  columnspan=3)

txt1 = Entry(width=10, bg="#ffe3db", bd=0, font=("Times New Roman", 14))
txt1.grid(row=2, column=0, sticky=W+E, pady=5,  columnspan=3)

accept_button = Button(text="Ввод", font=("Times New Roman", 14), bd=1, activebackground="#ffd4db", relief=FLAT,
                       bg="#ffe3db", command=rab)
accept_button.grid(row=4, column=0, sticky=W+E, pady=5,  columnspan=3)

root.protocol("WM_DELETE_WINDOW, close")
root.mainloop()
