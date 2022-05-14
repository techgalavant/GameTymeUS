#!/usr/bin/env python2
# Rock, Paper, Scissors Video Game Module

from tkinter import *
import tkinter as tk
import random

def gui():

    rock = 1
    paper = 2
    scissors = 3

    names = {rock: "Rock", paper: "Paper", scissors: "Scissors"}
    rules = {rock: scissors, paper: rock, scissors: paper}

    def start():
        while game():
            pass

    def game():
        player = player_choice.get()
        computer = random.randint(1,3)
        computer_choice.set(names[computer])
        result(player, computer)

    def result(player, computer):
        new_score = 0
        if player == computer:
            result_set.set("Tie game.")
        else:
            if rules[player]==computer:
                result_set.set("Your victory has been assured.")
                new_score = player_score.get()
                new_score +=1
                player_score.set(new_score)
            else:
                result_set.set("You have been defeated by the computer!")
                new_score = computer_score.get()
                new_score += 1
                computer_score.set(new_score)

    rps_window = Toplevel()
    rps_window.title("Rock, Paper, Scissors")

    player_choice = IntVar()
    computer_choice = StringVar()
    result_set = StringVar()
    player_choice.set(1)
    player_score = IntVar()
    computer_score = IntVar()

    rps_frame = Frame(rps_window, padding = '3 3 12 12', width=300)
    rps_frame.grid(column=0, row=0, sticky=(N,W,E,S))
    rps_frame.columnconfigure(0, weight=1)
    rps_frame.rowconfigure(0, weight=1)

    Label(rps_frame, text='Player').grid(column=1, row=1, sticky=W)
    Radiobutton(rps_frame, text='Rock', variable=player_choice, value=1).grid(column=1, row=2, sticky=W)
    Radiobutton(rps_frame, text='Paper', variable=player_choice, value=2).grid(column=1, row=3, sticky=W)
    Radiobutton(rps_frame, text='Scissors', variable=player_choice, value=3).grid(column=1, row=4, sticky=W)

    Label(rps_frame, text='Computer').grid(column=3, row=1, sticky=W)
    Label(rps_frame, textvariable= computer_choice).grid(column=3, row=3, sticky=W)

    Button(rps_frame, text='Play', command=start()).grid(column=2, row=2)

    Label(rps_frame, text='Score').grid(column=1, row=5, sticky=W)
    Label(rps_frame, textvariable= player_score).grid(column=1, row=6, sticky=W)

    Label(rps_frame, text='Score').grid(column=3, row=5, sticky=W)
    Label(rps_frame, textvariable= computer_score).grid(column=3, row=6, sticky=W)

    Label(rps_frame, textvariable= result_set).grid(column=2, row=7)

if __name__ == '__main__':
    gui()