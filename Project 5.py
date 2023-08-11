import random

DiceRolling = True

while DiceRolling:
    print(random.randint(1,6))
    PlayAgain = input('Do you want to roll again? [Y/N]: ')
    if PlayAgain == 'y':
        continue
    else:
        print('Gave Over')
        break