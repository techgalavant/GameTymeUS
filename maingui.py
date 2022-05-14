#!/usr/bin/env python2
#  This will create a window dialog interface for the games

from tkinter import *

import hangman
import rpszr2

root = Tk()
root.title("Games Collection")

mainframe = Frame(root, height=200, width=500)
mainframe.pack_propagate(0)
mainframe.pack(padx=5, pady=5)

intro = Label(mainframe, text="Select an option below:""")
intro.pack(side=TOP)

rps_button = Button(mainframe, text="Rock, Paper, Scissors", command=rpszr2.gui)
rps_button.pack()

hm_button = Button(mainframe, text="Hangman", command=hangman.start())
hm_button.pack()

exit_button = Button(mainframe, text="Quit", command=root.destroy)
exit_button.pack(side=BOTTOM)

root.mainloop()