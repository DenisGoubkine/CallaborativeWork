import math
from tkinter.constants import E
speeda= int(input('How was is car A going?: '))
speedb= int(input('How was is car b going?: '))

speed=(speeda+speedb)/2
print(f'It will take them {round((100/speed), 2)} hours for the two cars to meet')
