#!python3
#-*- coding:utf-8 -*-

import selenium
from tkinter import *

__ver__ = "2022. 12. 31"

# GUI Functions
def getId():
    id = inputId.get("1.0", "end-1c")

    return id


def getPw():
    pw = inputPw.get("1.0", "end-1c")

    return pw


def changeText(textType):
    if textType == 1:
        nowText.set("ID 또는 PW가 입력되어 있지 않습니다.")
    elif textType == 2:
        nowText.set("ID 또는 PW가 올바르지 않습니다.")
    elif textType == 3:
        nowText.set("조건에 해당하는 문제가 없습니다.")


def findNum(tag, tier):
    

    return 0


def process():
    id = getId()
    pw = getPw()

    if id == '' or pw == '':
        changeText(1)
    else:
        num = findNum(0, 0)

        if num == '-1': 
            changeText(2)
        else:
            inputProblemNum.delete("1.0", "end")
            inputProblemNum.insert("1.0", num)

    
# GUI Setting
gui = Tk()

gui.title("Solved.ac 랜덤 문제 추출 " + __ver__)
gui.geometry('400x200+100+100')
gui.resizable(False, False)

informId = Label(gui, text = "ID 입력", font = ('현대하모니 L', 12, 'bold'), width = 5)
informId.grid(row = 0, column = 0, padx = 10)

inputId = Text(gui, width = 20, height = 2)
inputId.configure(font = ('현대하모니 L', 10))
inputId.grid(row = 0, column = 1)

informPw = Label(gui, text = "PW 입력", font = ('현대하모니 L', 12, 'bold'))
informPw.grid(row = 1, column = 0, padx = 10)

inputPw = Text(gui, width = 20, height = 2)
inputPw.configure(font = ('현대하모니 L', 10))
inputPw.grid(row = 1, column = 1)

informCondition = Label(gui, text = "문제 탐색 조건 입력", font = ('현대하모니 L', 12, 'bold'))
informCondition.grid(row = 2, column = 0, padx = 10)

inputCondition = Text(gui, width = 20, height = 2)
inputCondition.configure(font = ('현대하모니 L', 10))
inputCondition.grid(row = 2, column = 1)

informProblemNum = Label(gui, text = "문제 번호 출력", font = ('현대하모니 L', 12, 'bold'))
informProblemNum.grid(row = 3, column = 0, padx = 10)

inputProblemNum = Text(gui, width = 20, height = 2)
inputProblemNum.configure(font = ('현대하모니 L', 10))
inputProblemNum.grid(row = 3, column = 1)

nowText = StringVar()
nowText.set("")
informText = Label(gui, textvariable = nowText, font = ('현대하모니 L', 8))
informText.grid(row = 4)

button = Button(gui, text = "Find", command = process)
button.grid(row = 5)

gui.mainloop()