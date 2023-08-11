answer = input('Do you want to play this game? [Yes/No]:')

if answer == 'yes':
    print('Welcome to the game!')
    answer = input('Do you want to go to jungle/cave? [Jungle/Cave]:')
    if answer == 'jungle':
        print('you see the hungry tiger! the tiger will eat you')
    elif answer == 'cave':
        print('you see the bear in front of the cave')
        answer = input('do you want to fight with be bear or run away? [Fight/Run Away]')
        if answer == 'fight':
            print('bear is too strong! you lose the game')
        else:
            print('wow! still you are alive!')
else:
    print('The Game is closed')

