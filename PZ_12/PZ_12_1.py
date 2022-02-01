# Вариант 21.
# В соответствии с номером варианта перейти по ссылке на прототип. Реализовать
# его в IDE PyCharm Community с применением пакета tk. Получить интерфейс максимально
# приближенный к оригиналу.
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox

root = Tk()
root.title("Обработка формы")
root.geometry("450x420")


def close():
    root.destroy()
    root.quit


fr1 = Frame(bd=1, bg="white")
fr1.place(x=10, y=30, width=430, height=380)

lab0 = Label(root, text="Форма регистрации пользователя", font=("Arial", 15))
lab1 = Label(fr1, text="Ваше имя: ", font=("Arial", 10), bg="white")
lab2 = Label(root, text="Пароль: ", font=("Arial", 10), bg="white")
lab3 = Label(root, text="Возраст: ", font=("Arial", 10), bg="white")
lab4 = Label(root, text="Пол: ", font=("Arial", 10), bg="white")
lab5 = Label(root, text="Ваши увлечения: ", font=("Arial", 10), bg="white")
lab6 = Label(root, text="Ваша страна: ", font=("Arial", 10), bg="white")
lab7 = Label(root, text="Ваш город: ", font=("Arial", 10), bg="white")
lab8 = Label(root, text="Кратко о себе: ", font=("Arial", 10), bg="white")
lab9 = Label(root, text="Решите пример, запишите результат в поле ниже: ", font=("Arial", 10), bg="white")

lab0.place(x=80, y=0)  # Заголовок
lab1.place(x=0, y=5)  # Имя
lab2.place(x=10, y=65)  # Пароль
lab3.place(x=10, y=95)  # Возраст
lab4.place(x=10, y=125)  # Пол
lab5.place(x=10, y=155)  # Увлечения
lab6.place(x=10, y=185)  # Страна
lab7.place(x=10, y=215)  # Город
lab8.place(x=10, y=245)  # Кратко о себе
lab9.place(x=10, y=315)  # Пример

txt1 = Entry(root, width=45, bg="lightgrey", bd=0)
txt2 = Entry(root, width=45, bg="lightgrey", bd=0)
txt3 = Entry(root, width=45, bg="lightgrey", bd=0)
txt4 = Text(root, height=3, width=34, wrap=WORD, bg="lightgrey", bd=0)  # Ввод текста
txt5 = Entry(root, width=45, bg="lightgrey", bd=0)

txt1.place(x=160, y=40)
txt2.place(x=160, y=70)
txt3.place(x=160, y=100)
txt4.place(x=160, y=250)
txt5.place(x=160, y=350)

mg = Label(root, text="Мужской", bg="white")
jg = Label(root, text="Женский", bg="white")

mg.place(x=157, y=130)
jg.place(x=350, y=130)

rad1 = Radiobutton(root, bd=0, value=1, bg="white")
rad2 = Radiobutton(root, bd=0, value=2, bg="white")

rad1.place(x=230, y=130)
rad2.place(x=415, y=130)

lab10 = Label(root, text="Музыка", font=("Arial", 10), bd=0, bg="white")
lab10.place(x=160, y=160)
ch = Checkbutton(root, bg="white")
ch.place(x=210, y=160)

lab11 = Label(root, text="Видео", font=("Arial", 10), bg="white")
lab11.place(x=250, y=160)
ch = Checkbutton(root, bg="white")
ch.place(x=300, y=160)

lab12 = Label(root, text="Рисование", font=("Arial", 10), bg="white")
lab12.place(x=340, y=160)
ch = Checkbutton(root, bg="white")
ch.place(x=410, y=160)

list1 = Combobox(root, height=3, width=36, font=("Arial", 10))
list1['values'] = ("Россия", "Чехия", "Польша", "Китай")
list1.current(1)

list2 = Combobox(root, height=3, width=36, font=("Arial", 10))
list2['values'] = ("Москва", "Прага", "Варшава", "Пекин")
list2.current(1)

list1.place(x=160, y=190)
list2.place(x=160, y=220)

but1 = Button(root, text="Отменить ввод", bg="lightgrey", bd=0, font=("Arial", 10), width=14)
but2 = Button(root, text="Данные подтверждаю", bg="lightgrey", bd=0, font=("Arial", 10))

but1.place(x=160, y=380)
but2.place(x=290, y=380)

root.protocol("WM_DELETE_WINDOW, close")
root.mainloop()
