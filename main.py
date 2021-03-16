import random
from colorama import *

bandymai = 0
max = 5
while True:

    x = random.randint(1, 10)
    y = random.randint(1, 10)
    teisingas = x * y
    print('Kiek bus ' + str(x) + ' padauginus is ' + str(y) + '?')
    atsakimas = int(input('Įrašyk atsakymą:- '))

    if atsakimas == teisingas:
        bandymai += 1
        print(Fore.GREEN + 'Šaunuolė! Teisingai!')
        print('Liko {} klausimai'.format(max-bandymai))
        print(Style.RESET_ALL)
        if bandymai == 5:
            print(Fore.GREEN, Back.WHITE + 'Atesakei teisingai net {} kartus iš eilės.\nGali pailsėti!'.format(bandymai))
            break
        else:
            pass
    else:
        print(Fore.RED + 'NETEISINGAI!. Teisingas atsakymas: {}'.format(teisingas))
        print(f'Atsakei teisingai tik {bandymai} kartus iš eilės.')
        break
