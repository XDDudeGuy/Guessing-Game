from typing import Tuple
from rng import rand_num as rng
import PySimpleGUI as sg

sg.theme('Dark Amber')

def checker(answer: int, guess: int) -> Tuple[bool, str]:
    if answer == guess:
        return (True, "")
    if answer > guess:
        return (False, "Higher!")
    if answer < guess:
        return (False, "Lower!")


layout = [[sg.Text("Guess a number from 1 to 1000:")],
[sg.InputText(key="--INPUT--"), sg.Button("Submit"), sg.Button("Close")],
[sg.Text("", key="--OUTPUT--")]]

window = sg.Window(title="   Guessing Game", layout=layout)

answer = rng(1, 1000)

while True:
    event, values = window.read()
    if event == "Close" or event == sg.WIN_CLOSED or event == sg.WIN_CLOSE_ATTEMPTED_EVENT:
        break
    if event == "Submit":
        is_answer, output = checker(answer, int(values["--INPUT--"]))
        if is_answer:
            window["--OUTPUT--"].update("YOU WIN!")
        else:
            window["--OUTPUT--"].update(output)

window.close()