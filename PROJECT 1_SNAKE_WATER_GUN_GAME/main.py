# the game has S - representing the Snake ; W representing the Water ; G representing the Gun 


import random

def swg(comp, mine):
    if(comp == mine):
        return None
    if(comp =='S' and mine == 'G'):
        return True
    elif(comp =='W' and mine == 'S'):
        return True
    elif(comp =='G' and mine == 'W'):
        return True
    else:
        return False
    

    
choice = ('S', 'W', 'G')
comp = random.randint(0,2)
comp = choice[comp]
mine = input('Choose either S, W or G: ')

win = swg(comp, mine)
if win is None:
    print(f"You chose {mine} and the computer chose {comp}")
    print("You are  in a draw !!")
elif win:
    print(f"You chose {mine} and the computer chose {comp}")
    print("You won")
else:
    print(f"You chose {mine} and the computer chose {comp}")
    print("You Loose")
    




