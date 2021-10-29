import random
from tkinter import Event
from tkinter import Tk, font
from tkinter.constants import DISABLED
import PySimpleGUI as sg
from colour import Color
sg.theme('LightBrown11')
def main():

    # GAME LOGIC VARIABLES
    miles_travelled = 0
    thirst = 0
    camel_tiredness = 0
    distance_natives = -15
    drinks = 3

    # DEF STATMENTS
    BLUE = Color("blue")
    YELLOW = Color("yellow")
    RED = Color("red")

    layout = [
        [sg.Text('Welcome To My Camel Game!', size=(60, 1), justification='centre', font=("High Tower Text", 25), text_color=RED)],
        [sg.Text("You have stolen a camel to make your way across the great Mobi desert.", size=(60, 1), justification='centre', font=('High Tower Text', 12), text_color=RED)],
        [sg.Text("The natives want their camel back and are chasing you down!", size=(60, 1), justification='centre', font=('High Tower Text', 12), text_color=RED)],
        [sg.Text("Survive your desert trek and out run the natives.", size=(60, 1), justification='centre', font=('High Tower Text', 12), text_color=RED)],

        [sg.Text("Status:", font=("Arial Black", 15)), sg.Text(key="_OUT_")],
        [sg.Text("Risk:", font=("Arial Black", 15)), sg.Text(key="_OUT2_")],
        [sg.Text("Game Status:", font=("Arial Black", 15)), sg.Text(key="_OUT3_")],

        [sg.Text("        ")],
        [sg.Button("A: Drink from your canteen.", font=("High Tower Text", 15), disabled=False)],
        [sg.Button("B: Ahead moderate speed.", font=("High Tower Text", 15), disabled=False)],
        [sg.Button("C: Ahead full speed.", font=("High Tower Text", 15), disabled=False)],
        [sg.Button("D: Stop for the night.", font=("High Tower Text", 15), disabled=False)],
        [sg.Button("E: Status check.", font=("High Tower Text", 15), disabled=False)],
        [sg.Text("        ")],
        [sg.Button("Q: Quit"), sg.Button("P: Play Again")],
    ]

    window = sg.Window("Start", layout, size=(620, 650))

    done = False
    while not done:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == "Q: Quit":
            done = True

        elif event == "P: Play Again":
            window.close()
            main()

        elif event == "A: Drink from your canteen.":
            if drinks:
                thirst = 0
                drinks -= 1
                window["_OUT_"].update("You feel refreshed.")
                window["_OUT2_"].update('')
            else:
                window["_OUT_"].update("Your canteen is empty.")

        elif event == "B: Ahead moderate speed.":
            miles_travelled += random.randint(5, 12)
            thirst += 1
            camel_tiredness += 1
            distance_natives += random.randint(7, 14)
            window["_OUT_"].update(f' You have travelled {miles_travelled} miles')

        elif event == ("C: Ahead full speed."):
            miles_travelled += random.randint(10, 20)
            window["_OUT_"].update(f' You have travelled {miles_travelled} miles')
            thirst += 1
            camel_tiredness += random.randint(1, 3)
            distance_natives += random.randint(7, 14)

        elif event == "D: Stop for the night.":
            camel_tiredness = 0
            distance_natives += random.randint(7, 14)
            window["_OUT_"].update(f"You and the camel had a good night's rest.\nThe natives are {distance_natives} miles behind you!")
            window["_OUT2_"].update('')

        elif event == "E: Status check.":
            window["_OUT_"].update(f'\n\nMiles traveled:{miles_travelled} \nDrinks in canteen:{drinks} \nThe natives are {distance_natives} miles behind you. ')

        alive = True
        win = False

        if thirst > 4 and thirst <= 6:
            window["_OUT2_"].update('You are thirsty.')
        elif thirst > 6:
            alive = False
            window["_OUT3_"].update('You have died of thirst.')
            window["_OUT2_"].update('')
            window["_OUT_"].update('')
            window.find_element("A: Drink from your canteen.").Update(disabled=True)
            window.find_element("B: Ahead moderate speed.").Update(disabled=True)
            window.find_element("C: Ahead full speed.").Update(disabled=True)
            window.find_element("D: Stop for the night.").Update(disabled=True)
            window.find_element("E: Status check.").Update(disabled=True)

        elif camel_tiredness > 5 and camel_tiredness <= 8:
            window["_OUT2_"].update('Your camel is getting tired.')

        elif camel_tiredness > 8:
            alive = False
            window["_OUT3_"].update('Your camel has died of exhaustion,\nand now you are stranded in the desert.')
            window["_OUT2_"].update('')
            window["_OUT_"].update('')
            window.find_element("A: Drink from your canteen.").Update(disabled=True)
            window.find_element("B: Ahead moderate speed.").Update(disabled=True)
            window.find_element("C: Ahead full speed.").Update(disabled=True)
            window.find_element("D: Stop for the night.").Update(disabled=True)
            window.find_element("E: Status check.").Update(disabled=True)

        elif distance_natives >= miles_travelled:
            window["_OUT3_"].update('The natives have caught up and captured you.')
            alive = False
            window["_OUT2_"].update('')
            window["_OUT_"].update('')
            window.find_element("A: Drink from your canteen.").Update(disabled=True)
            window.find_element("B: Ahead moderate speed.").Update(disabled=True)
            window.find_element("C: Ahead full speed.").Update(disabled=True)
            window.find_element("D: Stop for the night.").Update(disabled=True)
            window.find_element("E: Status check.").Update(disabled=True)

        elif (miles_travelled-distance_natives) < 15:
            window["_OUT2_"].update('The natives are getting close!')

        if miles_travelled >= 200 and alive:
            window["_OUT3_"].update('You got out of the desert and escaped the natives!')
            window["_OUT2_"].update('')
            window["_OUT_"].update('')
            window.find_element("A: Drink from your canteen.").Update(disabled=True)
            window.find_element("B: Ahead moderate speed.").Update(disabled=True)
            window.find_element("C: Ahead full speed.").Update(disabled=True)
            window.find_element("D: Stop for the night.").Update(disabled=True)
            window.find_element("E: Status check.").Update(disabled=True)

        if random.randint(1, 2) == 1 and miles_travelled > 0 and win is False:
            window["_OUT_"].update("You have found an oasis!\n You and your camel are very refreshed.")
            thirst = 0
            camel_tiredness = 0
            drinks = 10

    window.close()

main()
