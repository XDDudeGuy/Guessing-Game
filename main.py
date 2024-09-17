from typing import Tuple # Allows the usage of the Tuple type in our checker function
from random import randint, seed
import PySimpleGUI as sg

def checker(answer: int, guess: int) -> Tuple[bool, str]:
    if answer == guess:
        return (True, "")
    if answer > guess:
        return (False, "Higher!")
    if answer < guess:
        return (False, "Lower!")

def main():
    sg.theme('Dark Amber') # Sets the theme for the gui
    
    layout = [[sg.Text("Guess a number from 1 to 1000:")],
    [sg.InputText(key="--INPUT--"), sg.Button("Submit"), sg.Button("Close")],
    [sg.Text("", key="--OUTPUT--")]] # Defines how our window should be layed out

    window = sg.Window(title="  Guessing Game", layout=layout) # Creates the window 

    #Randomizes more
    for _ in range(0,10):
        seed(randint(0,10000))
    answer = randint(1,1000)

    while True:
        event, values = window.read()
        if event == "Close" or event == sg.WIN_CLOSED or event == sg.WIN_CLOSE_ATTEMPTED_EVENT: # If the user tries to close the window
            break
        if event == "Submit": # if the user submits their answer
            is_answer, output = checker(answer, int(values["--INPUT--"]))
            if is_answer:
                window["--OUTPUT--"].update("YOU WIN!")
            else:
                window["--OUTPUT--"].update(output)

    window.close() # closes the window

if __name__ == "__main__":
    main()