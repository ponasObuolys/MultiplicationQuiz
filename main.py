import random
from colorama import *

bandymai = int(input(Fore.YELLOW +'\nKelis kartus nori spėti?- '))
print(Style.RESET_ALL)
maximum = bandymai - 1

while True:

    x = random.randint(2, 9)
    y = random.randint(2, 9)
    teisingas = x * y
    print('|---------------------------------|')
    print('\tKiek bus ' + str(x) + ' padauginus is ' + str(y) + '?')
    atsakimas = int(input(Fore.BLUE + '\tĮrašyk atsakymą ir paspausk ENTER:- '))
    print('|---------------------------------|')

    if atsakimas == teisingas:
        bandymai -= 1
        print(Fore.GREEN + '\tŠaunuolė! Teisingai!')
        print('\tLiko {} klausimai(-ų)'.format(bandymai))
        print(Style.RESET_ALL)
        if bandymai == 0:
            print(Fore.GREEN, Back.WHITE + 'Atesakei teisingai {} kartus iš eilės.\nGali pailsėti!'.format(maximum+1))
            break
        else:
            pass
    else:
        print(Fore.RED + '\nNETEISINGAI!. Teisingas atsakymas: ' + Fore.GREEN + '{}'.format(teisingas))
        print(Fore.RED + 'Atsakei teisingai tik {} kartus iš eilės.'.format(maximum+1))
        break
