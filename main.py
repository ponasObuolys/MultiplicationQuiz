import random
from colorama import *

bandymai = int(input(Fore.YELLOW +'\nKelis kartus nori spėti?- '))
print(Style.RESET_ALL)
spejimai = 0
atsakyti = []

while True:

    x = random.randint(2, 9)
    y = random.randint(2, 9)
    teisingas = x * y
    print('|------------------------------------------|')
    print('\tKiek bus ' + str(x) + ' padauginus is ' + str(y) + '?')
    atsakimas = int(input(Fore.BLUE + '\tĮrašyk atsakymą ir paspausk ENTER:- '))
    print('|------------------------------------------|')

    if atsakimas == teisingas:
        bandymai -= 1
        spejimai += 1
        atsakyti.append([f'{x} x {y} = {teisingas}'])
        print(Fore.GREEN + '\tŠaunuolė! Atsakei i {} klausymą(-us)'.format(spejimai))
        print(f'\tLiko {bandymai} klausimas(-ai)')
        print(Style.RESET_ALL)
        if bandymai == 0:
            stringas = ' '.join([str(elem) for elem in atsakyti])
            print(Fore.MAGENTA + 'Atsakei teisingai {} kartus(-ų) iš eilės.'.format(spejimai))
            print(Fore.YELLOW + 'Teisingi atsakymai buvo šie: {}'.format(stringas))
            break
        else:
            pass
    else:
        print(Fore.RED + '\nNETEISINGAI!. Teisingas atsakymas: ' + Fore.GREEN + '{}'.format(teisingas))
        print(Fore.RED + 'Atsakei teisingai tik {} kartą(-us) iš eilės.'.format(spejimai))
        break
