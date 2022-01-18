#!python3
#-*- coding:utf-8 -*-

__version__ == '2021. 10. 06'

import urllib.parse
from tkinter import *

# Method
def decode():
    url = line.get("1.0", "end-1c")

    cpOutput.delete("1.0", "end")
    utfOutput.delete("1.0", "end")
    cpOutput.insert("1.0", cpDecode(url))
    utfOutput.insert("1.0", utfDecode(url))


def cpDecode(decode_string):
    return urllib.parse.unquote(decode_string, encoding = 'CP949')


def utfDecode(decode_string):
    return urllib.parse.unquote(decode_string, encoding = 'utf-8')


# GUI Setting with tkinter
gui = Tk()

gui.title("Decoder " + __version__)
gui.geometry('400x600+100+100')
gui.resizable(False, False)

intro = Label(gui, text = "변환 값 입력", font = ('현대하모니 L', 14, 'bold'))
intro.grid(row = 0, column = 0, padx = 10)

line = Text(gui, width = 50, height = 10)
line.configure(font = ('현대하모니 L', 10))
line.gird(row = 1, column = 0, padx = 23, pady = 10)

conversion = Button(gui, text = "변환", command = decode)
conversion.grid(row = 2, column = 0)

cpIntro = Label(gui, text = "CP959 변환", font = ('현대하모니 L', 12))
cpIntro.grid(row = 3, column = 0)

cpOutput = Text(gui, width = 50, height = 8)
cpOutput.configure(font = ('현대하모니 L', 10))
cpOutput.grid(row = 4, column = 0, padx = 23, pady = 10)

utfIntro = Label(gui, text = "UTF-8 변환", font = ('현대하모니 L', 12))
utfIntro.grid(row = 5, column = 0)

utfOutput = Text(gui, width = 50, height = 8)
utfOutput.configure(font = ('현대하모니 L', 10))
utfOutput.grid(row = 6, column = 0, padx = 23, pady = 10)

gui.mainloop()