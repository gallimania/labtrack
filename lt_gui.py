# Copyright (C) 2018 Garrett Fifer
#
# This file provided the functions that supply the main program with an easy to
# use graphical user interface. Uses the tkinter package supplied with most python
# installations by default.
#
# begin lt_gui.py
# 

from tkinter import Tk, Label, Button, OptionMenu, Entry


rootwindow = Tk()

def main_window():
  Label(rootwindow, text='LabTrack GUI').grid(row=0, column=0)
 
def add_new():
  addnew_win = TopLevel(rootwindow)
  Label(addnew_win, text='Item Category: ').grid(row=0, column=0)

mainloop()
