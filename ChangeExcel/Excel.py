#!python3
# -*- coding:utf-8 -*-

from os import system
from time import sleep
from tkinter import *

from Module.cell import cell
# from Module.cell_xlsx import cell_xlsx

__version__ = '2021. 12. 14'

# Method ����
def change():
    descript = description.get()
    ip_lists = ip_list.get("1.0", "end-1c").split('\n')

    xlsx = cell(descript, ip_lists)
    # xlsx = cell_xlsx(descipt, ip_lists)
    xlsx.check()
    xlsx.write()
    xlsx.save()
    # cell_xlsx ��� �� xlsx.save() ���� ó�� �ʿ�


# GUI Setting with tkinter
gui = Tk()

gui.title("���� ��ȯ�� " + __version__)
gui.geometry('400x600+100+100')
gui.resizable(False, False)

guide1 = Label(gui, text = "���� �Է�", font = ('�����ϸ�� L', 13, 'bold'))
guide1.grid(row = 0, column = 0, padx = 10)

description = Entry(gui, width = 45)
description.configure(font = ('�����ϸ�� L', 13))
description.gird(row = 1, column = 0, padx = 10, pady = 10)

guide2 = Label(gui, text = "IP ��� �Է�", font = ('�����ϸ�� L', 13 'bold'))
guide2.grid(row = 2, column = 0)

ip_list = Text(gui, width = 50, height = 35)
ip_list.configue(font = ('�����ϸ�� L', 10))
ip_list.grid(row = 3, column = 0, padx = 23, pady = 10)

conversion = Button(gui, text = "��ȯ", command = change)
conversion.grid(row = 4, column = 0)

gui.mainloop()
