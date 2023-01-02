#!python3
#-*- coding:utf-8 -*-

import selenium
from tkinter import *

__ver__ = "2022. 12. 31"

# GUI Functions
def getId():
    id = "any"

    return id


def getPw():
    pw = "any"

    return pw


def setNum(num):
    pass


def process():
    id = getId()
    pw = getPw()

    num = 0

    setNum(num)


# GUI Setting
gui = Tk()

gui.title("Solved.ac 랜덤 문제 추출 " + __ver__)
gui.geometry('400x600+100+100')
gui.resizable(False, False)

informId = Label(gui, text = "ID 입력", font = ('현대하모니 L', 14, 'bold'))
infromId.grid(row = 0, column = 0, padx = 10)

inputId = Text(gui, width = 50, height = 10)
inputId.configure(font = ('현대하모니 L', 10))
inputId.grid(row = 1, column = 0)

informPw = Label(gui, text = "PW 입력", font = ('현대하모니 L', 14, 'bold'))
infromPw.grid(row = 0, column = 0, padx = 10)

inputPw = Text(gui, width = 50, height = 10)
inputPw.configure(font = ('현대하모니 L', 10))
inputPw.grid(row = 1, column = 0)

informProblemNum = Label(gui, text = "문제 번호 출력", font = ('현대하모니 L', 14, 'bold'))
infromProblemNum.grid(row = 0, column = 0, padx = 10)

inputProblemNum = Text(gui, width = 50, height = 10)
inputProblemNum.configure(font = ('현대하모니 L', 10))
inputProblemNum.grid(row = 1, column = 0)

gui.mainloop()