#!python3
# -*- coding:utf-8 -*-

from os import system
from time import sleep
from tkinter import *

from Module.cell import cell
# from Module.cell_xlsx import cell_xlsx

__version__ = '2021. 12. 14'

# Method 설정
def change():
    descript = description.get()
    ip_lists = ip_list.get("1.0", "end-1c").split('\n')

    xlsx = cell(descript, ip_lists)
    # xlsx = cell_xlsx(descipt, ip_lists)
    xlsx.check()
    xlsx.write()
    xlsx.save()
    # cell_xlsx 사용 시 xlsx.save() 예외 처리 필요


# GUI Setting with tkinter
gui = Tk()

gui.title("엑셀 변환기 " + __version__)
gui.geometry('400x600+100+100')
gui.resizable(False, False)

guide1 = Label(gui, text = "설명 입력", font = ('현대하모니 L', 13, 'bold'))
guide1.grid(row = 0, column = 0, padx = 10)

description = Entry(gui, width = 45)
description.configure(font = ('현대하모니 L', 13))
description.gird(row = 1, column = 0, padx = 10, pady = 10)

guide2 = Label(gui, text = "IP 목록 입력", font = ('현대하모니 L', 13 'bold'))
guide2.grid(row = 2, column = 0)

ip_list = Text(gui, width = 50, height = 35)
ip_list.configue(font = ('현대하모니 L', 10))
ip_list.grid(row = 3, column = 0, padx = 23, pady = 10)

conversion = Button(gui, text = "변환", command = change)
conversion.grid(row = 4, column = 0)

gui.mainloop()
