import random


print ('Welcome to Camel!\n')
print('You have stolen a camel to make your way across the great Mobi desert.\n ')
print('The natives want their camel back and are chasing you down!\n')
print('Survive your desert trek and out run the natives.\n')

miles_travelled= 0
thirst= 0
camel_tiredness= 0
distance_natives= -20
drinks= 10

done = False
while done == False:
    print('A. Drink from your canteen. \nB. Ahead moderate speed. \nC. Ahead full speed. \nD. Stop for the night. \nE. Status check. \nQ. Quit.\n')
    choice= input('Please select an option listed above: ')
    choice= choice.upper()
    print()
    if choice== 'Q':
        done= True
        print()

    elif choice== 'E':
        print(f'Miles traveled:{miles_travelled} \nDrinks in canteen:{drinks} \nThe natives are {abs(distance_natives)} miles behind you. ')
        print()
        
    elif choice== 'D': 
        camel_tiredness= 0
        print('Camel is happy\n')
        distance_natives += random.randrange(7, 15)
        print(f'The natives are {distance_natives} miles behind you!')
        print()

    elif choice == 'C':
        miles_travelled += random.randrange(10,21)
        print(f' You have travelled {miles_travelled} miles')
        thirst+=1
        camel_tiredness+= random.randrange(1,4)
        distance_natives+= random.randrange(7,15)
        print()

    elif choice == 'B':
        miles_travelled+= random.randrange(5,13)
        print(f'You have travelled {miles_travelled} miles')
        thirst+=1
        camel_tiredness+= 1
        distance_natives+= random.randrange(7,15)
        print()

    elif choice== 'A':
        if drinks > 0:
            thirst=0
            drinks-=1
            print()
        else:
            print('No drinks left')
            print()

    alive=True
    if thirst>4 and thirst<=6:
        print('You are thirsty')
        print()

    elif thirst>6:
        alive= False
        print('You have died of thirst')
        done= True
        print()

    elif camel_tiredness>5 and camel_tiredness<=8:
        print('Your camel is getting tired')
        print()

    elif camel_tiredness>8:
        alive= False
        print('Your camel is dead')
        done= True
        print()

    elif distance_natives>=miles_travelled:
        print('The native have caught you, well played')
        done= True
        alive= False
        print()

    elif (miles_travelled-distance_natives) < 15:
        print('The natives are getting close')
        print()

    elif miles_travelled >= 200 and alive== True: 
        print('You have crossed the dessert, you win')
        done= True

    oasis= random.randrange(1,21)
    if oasis == 1:
        print('You have found the oasis\n You are very refreshed')
        thirst= 0
        camel_tiredness= 0
        drinks= 10