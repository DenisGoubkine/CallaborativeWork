import random
from tkinter import Event
from tkinter.constants import DISABLED
import PySimpleGUI as sg
from colour import Color
sg.theme('LightBrown11')


def main():

    # GAME LOGIC VARIABLES
    miles_travelled = 0
    thirst = 0
    camel_tiredness = 0
    distance_natives = -20
    drinks = 10

    # DEF STATMENTS
    BLUE = Color("blue")
    YELLOW = Color("yellow")
    RED = Color("red")

    layout = [
        [sg.Text('Welcome To My Camel Game!!!', size=(60, 1), justification='centre', font=("Times New Roman", 25), text_color=RED)],
        [sg.Text("You have stolen a camel to make your way across the great Mobi desert.", size=(60, 1), justification='centre', font=('Helvetica', 12), text_color=RED)],
        [sg.Text("The natives want their camel back and are chasing you down!", size=(60, 1), justification='centre', font=('Helvetica', 12), text_color=RED)],
        [sg.Text("Survive your desert trek and out run the natives.", size=(60, 1), justification='centre', font=('Helvetica', 12), text_color=RED)],

        [sg.Text("Status:", font=("Arial Black", 15)), sg.Text(key="_OUT_")],
        [sg.Text("Risk:", font=("Arial Black", 15)), sg.Text(key="_OUT2_")],
        [sg.Text("Game Status:", font=("Arial Black", 15)), sg.Text(key="_OUT3_")],

        [sg.Text("        ")],
        [sg.Button("A: Drink from your canteen.", font=("Times New Roman", 15), disabled=False)],
        [sg.Button("B: Ahead moderate speed.", font=("Times New Roman", 15), disabled=False)],
        [sg.Button("C: Ahead full speed.", font=("Times New Roman", 15), disabled=False)],
        [sg.Button("D: Stop for the night.", font=("Times New Roman", 15), disabled=False)],
        [sg.Button("E: Status check.", font=("Times New Roman", 15), disabled=False)],
        [sg.Text("        ")],
        [sg.Button("Q: Quit"), sg.Button("P: Play Again")],
    ]

    window = sg.Window("Start", layout, size=(450, 550))

    done = False
    while not done:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == "Q: Quit":
            done = True

        elif event == "P: Play Again":
            window.close()
            main()

        elif event == "A: Drink from your canteen.":
            if drinks > 0:
                thirst = 0
                drinks -= 1
                window["_OUT_"].update("Water Replenished")
                window["_OUT2_"].update('')
            else:
                window["_OUT_"].update("No Water Remaining")

        elif event == "B: Ahead moderate speed.":
            miles_travelled += random.randrange(5, 13)
            thirst += 1
            camel_tiredness += 1
            distance_natives += random.randrange(7, 15)
            window["_OUT_"].update(f' You have travelled {miles_travelled} miles')

        elif event == ("C: Ahead full speed."):
            miles_travelled += random.randrange(10, 21)
            window["_OUT_"].update(f' You have travelled {miles_travelled} miles')
            thirst += 1
            camel_tiredness += random.randrange(1, 4)
            distance_natives += random.randrange(7, 15)

        elif event == "D: Stop for the night.":
            camel_tiredness = 0
            distance_natives += random.randrange(7, 15)
            window["_OUT_"].update(f'Your Camel Has Rested\nThe natives are {distance_natives} miles behind you!')
            window["_OUT2_"].update('')

        elif event == "E: Status check.":
            window["_OUT_"].update(f'\n\nMiles traveled:{miles_travelled} \nDrinks in canteen:{drinks} \nThe natives are {distance_natives} miles behind you. ')

        alive = True
        win = False

        if thirst > 4 and thirst <= 6:
            window["_OUT2_"].update('Your camel is getting thirsty')
        elif thirst > 6:
            alive = False
            window["_OUT3_"].update('You have Died')
            window["_OUT2_"].update('')
            window["_OUT_"].update('')

        elif camel_tiredness > 5 and camel_tiredness <= 8:
            window["_OUT2_"].update('Your camel is getting tired')
        elif camel_tiredness > 8:
            alive = False
            window["_OUT3_"].update('You have Died')
            window["_OUT2_"].update('')
            window["_OUT_"].update('')
            window.FindElement("A: Drink from your canteen.").Update(disabled=True)
            window.FindElement("B: Ahead moderate speed.").Update(disabled=True)
            window.FindElement("C: Ahead full speed.").Update(disabled=True)
            window.FindElement("D: Stop for the night.").Update(disabled=True)
            window.FindElement("E: Status check.").Update(disabled=True)

        elif distance_natives >= miles_travelled:
            window["_OUT3_"].update('The natives have caught you, well played')
            alive = False
            window["_OUT2_"].update('')
            window["_OUT_"].update('')
            window.FindElement("A: Drink from your canteen.").Update(disabled=True)
            window.FindElement("B: Ahead moderate speed.").Update(disabled=True)
            window.FindElement("C: Ahead full speed.").Update(disabled=True)
            window.FindElement("D: Stop for the night.").Update(disabled=True)
            window.FindElement("E: Status check.").Update(disabled=True)

        elif (miles_travelled-distance_natives) < 15:
            window["_OUT2_"].update('The natives are getting close')

        if miles_travelled >= 200 and alive:
            window["_OUT3_"].update('You have crossed the dessert, you win')
            window["_OUT2_"].update('')
            window["_OUT_"].update('')
            window.FindElement("A: Drink from your canteen.").Update(disabled=True)
            window.FindElement("B: Ahead moderate speed.").Update(disabled=True)
            window.FindElement("C: Ahead full speed.").Update(disabled=True)
            window.FindElement("D: Stop for the night.").Update(disabled=True)
            window.FindElement("E: Status check.").Update(disabled=True)

        if random.randrange(1, 21) == 1 and miles_travelled > 0 and win is False:
            window["_OUT_"].update("You have found the oasis\n You are very refreshed")
            thirst = 0
            camel_tiredness = 0
            drinks = 10

    window.close()

main()
