import random
import time
from colorama import *
import math


def matematika():
    try:
        print(Fore.RED + '\t|- Sudėties testas -|')
        bandymai = int(input(Fore.YELLOW + '\tKelis kartus nori spręsti? (15/30/50)- '))
        if bandymai in [2, 15, 30, 50]:
            print(Style.RESET_ALL)
            spejimai = 0
            atsakyti = []
            testo_pradzia = time.time()
            kartojimas_teigiami = ['t', 'taip', 'teip', 'y', 'yes', 'ok']

            while True:
                x = random.randint(11, 99)
                y = random.randint(11, 99)
                teisingas = x + y
                dabar = time.time()
                uzgaista = math.ceil(dabar - testo_pradzia)

                print('|------------------------------------------|')
                print('\tKiek bus ' + str(x) + ' + ' + str(y) + '?')
                atsakimas = int(input(Fore.BLUE + '\tĮrašyk atsakymą ir paspausk ENTER:- '))
                print('|------------------------------------------|')
                if atsakimas == teisingas:
                    bandymai -= 1
                    spejimai += 1
                    atsakyti.append([f'{x} + {y} = {teisingas}'])
                    print(Fore.GREEN + f'\tPuiku! Atsakei i {spejimai} klausymų(-us)')
                    print(f'\tLiko {bandymai} klausimų(-ai)')
                    print(Style.RESET_ALL)
                    if bandymai == 0:
                        print('Testas išspręstas ' + Fore.RED + f'per: {uzgaista} sek.')
                        print(Fore.MAGENTA + 'Atsakei teisingai {} kartų(-us) iš eilės.'.format(spejimai))
                        print(Fore.YELLOW + 'Teisingi atsakymai buvo šie:')
                        print(*atsakyti, sep="\n")
                        kartojimas = input(Fore.GREEN + '\nNori bandyti dar kartą? (T/N)- ').lower()
                        if kartojimas in kartojimas_teigiami:
                            matematika()
                        else:
                            break
                    else:
                        pass
                else:
                    print('\nNETEISINGAI! ' + Fore.RED +  'Teisingas atsakymas: ' + Fore.GREEN + '{}'.format(teisingas))
                    print(Fore.RED + 'Atsakei teisingai tik {} kartą(-us) iš eilės.'.format(spejimai))
                    if spejimai > 0:
                        print(Fore.YELLOW + 'Teisingi atsakymai buvo šie:')
                        print(*atsakyti, sep="\n")
                        print('\nTestas neišspręstas. ' + Fore.RED + f'Užtrukai: {uzgaista} sek.')
                        print(Style.RESET_ALL)
                    else:
                        pass
                    kartojimas = input(Fore.GREEN + 'Nori bandyti dar kartą? (T/N)- ').lower()
                    if kartojimas in kartojimas_teigiami:
                        matematika()
                    else:
                        break
        else:
            print(
                'Galima rinktis iš' + Fore.RED + ' 15' + Fore.YELLOW + ',' + Fore.RED +
                ' 30' + Fore.YELLOW + ' arba' + Fore.RED + ' 50' + Fore.YELLOW + ' spėjimų')
            matematika()
    except ValueError:
        print('Atsakymas negali būti raidė!')
        matematika()

matematika()