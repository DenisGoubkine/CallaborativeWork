from calendar import TUESDAY
import random
from tkinter import Event
import PySimpleGUI as sg
from colour import Color

sg.theme('DarkPurple6')

miles_travelled= 0
thirst= 0
camel_tiredness= 0
distance_natives= -20
drinks= 10

# DEF STATMENTS

c= Color("blue")
y= Color("yellow")
r= Color("red")

layout = [

    [sg.Text('Welcome To My Camel Game, ENJOY!!!', size=(50, 1), font=("Times New Roman", 15), text_color=r)],
    [sg.Text("You have stolen a camel to make your way across the great Mobi desert.")],
    [sg.Text("The natives want their camel back and are chasing you down!")],
    [sg.Text("Survive your desert trek and out run the natives.")],

    [sg.Text("Status:"), sg.Text(key="_OUT_")],
    [sg.Text("Risk:"), sg.Text(key="_OUT2_")],
    [sg.Text("Game Status:"), sg.Text(key="_OUT3_")],

    [sg.Text("        ")],
    [sg.Button("A: Drink from your canteen.")],
    [sg.Button("B: Ahead moderate speed.")],
    [sg.Button("C: Ahead full speed.")],
    [sg.Button("D: Stop for the night.")],
    [sg.Button("E: Status check.")],
    [sg.Button("Q: Quit")],

    # [sg.Input(key='_IN_')],
    # [sg.Button("Confirm"), sg.Button("Cancel")]
]



window= sg.Window("Start", layout, size=(1400, 600))

done = False
while done == False:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED or event== "Q: Quit":
        done= True

    elif event== "A: Drink from your canteen.":
        if drinks > 0:
            thirst=0
            drinks-=1
            window["_OUT_"].update("Water Replenished")
            window["_OUT2_"].update('')
        else:
            window["_OUT_"].update("No Water Remaining")
   
    elif event== "B: Ahead moderate speed.":
        miles_travelled+= random.randrange(5,13)
        thirst+=1
        camel_tiredness+= 1
        distance_natives+= random.randrange(7,15)
        window["_OUT_"].update(f' You have travelled {miles_travelled} miles')
 
    elif event == ("C: Ahead full speed."):
        miles_travelled += random.randrange(10,21)
        window["_OUT_"].update(f' You have travelled {miles_travelled} miles')
        thirst+=1
        camel_tiredness+= random.randrange(1,4)
        distance_natives+= random.randrange(7,15)
   
    elif event == "D: Stop for the night.":
        camel_tiredness= 0
        distance_natives += random.randrange(7, 15)
        window["_OUT_"].update(f'Your Camel Has Rested\nThe natives are {distance_natives} miles behind you!')
        window["_OUT2_"].update('')

    elif event == "E: Status check.":
        window["_OUT_"].update(f'\n\nMiles traveled:{miles_travelled} \nDrinks in canteen:{drinks} \nThe natives are {distance_natives} miles behind you. ')

    alive= True

    if thirst>4 and thirst<=6:
        window["_OUT2_"].update('Your camel is getting thirsty')
    elif thirst>6:
        alive= False
        window["_OUT3_"].update('You have Died')
        window["_OUT2_"].update('')
        window["_OUT_"].update('')


    elif camel_tiredness>5 and camel_tiredness<=8:
        window["_OUT2_"].update('Your camel is getting tired')
    elif camel_tiredness>8:
        alive= False
        window["_OUT3_"].update('You have Died')
        # done= True
        window["_OUT2_"].update('')
        window["_OUT_"].update('')

    elif distance_natives>=miles_travelled:
        window["_OUT3_"].update('The natives have caught you, well played')
        # done= True
        alive= False
        window["_OUT2_"].update('')
        window["_OUT_"].update('')

    elif (miles_travelled-distance_natives) < 15:
        window["_OUT2_"].update('The natives are getting close')
    
    elif miles_travelled >= 200 and alive== True: 
        window["_OUT3_"].update('You have crossed the dessert, you win')
        # done= True
        window["_OUT2_"].update('')
        window["_OUT_"].update('')

    oasis= random.randrange(1,21)
    if oasis == 1:
        window["_OUT_"].update('You have found the oasis\n You are very refreshed')
        thirst= 0
        camel_tiredness= 0
        drinks= 10




window.close()

