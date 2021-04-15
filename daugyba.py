import random
import time
from colorama import *
import math


def matematika():
    try:
        print(Fore.RED + '\t|- Daugybos lentelės testas -|')
        bandymai = int(input(Fore.YELLOW + '\tKelis kartus nori spręsti? (15/30/50)- '))
        if bandymai in [2, 15, 30, 50]:
            print(Style.RESET_ALL)
            spejimai = 0
            atsakyti = []
            testo_pradzia = time.time()
            kartojimas_teigiami = ['t', 'taip', 'teip', 'y', 'yes', 'ok']

            while True:
                x = random.randint(2, 9)
                y = random.randint(2, 9)
                teisingas = x * y
                dabar = time.time()
                uzgaista = math.ceil(dabar - testo_pradzia)

                print('|------------------------------------------|')
                print('\tKiek bus ' + str(x) + ' padauginus iš ' + str(y) + '?')
                atsakimas = int(input(Fore.BLUE + '\tĮrašyk atsakymą ir paspausk ENTER:- '))
                print('|------------------------------------------|')
                if atsakimas == teisingas:
                    bandymai -= 1
                    spejimai += 1
                    atsakyti.append([f'{x} x {y} = {teisingas}'])
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
                            lentele()
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
                        lentele()
        else:
            print(
                'Galima rinktis iš' + Fore.RED + ' 15' + Fore.YELLOW + ',' + Fore.RED +
                ' 30' + Fore.YELLOW + ' arba' + Fore.RED + ' 50' + Fore.YELLOW + ' spėjimų')
            matematika()
    except ValueError:
        print('Atsakymas negali būti raidė!')
        matematika()


def lentele():
    while True:
        kartojimas_teigiami = ['t', 'taip', 'teip', 'y', 'yes', 'ok']
        skaiciai = list(range(1, 10))
        print(Fore.BLUE + '\nPasikartosime daugybos lentelę.')
        skaicius = int(input(Fore.RED + 'Kokio skaičiaus ' + Fore.BLUE + 'daugybos lentelę norėtum pasikartoti?- '))
        multiplied_list = [element * skaicius for element in skaiciai]
        print(Style.RESET_ALL)

        print(f'Daugybos lentelė iš {skaicius}')
        print(f'{skaicius} x {skaiciai[0]} = {multiplied_list[0]}')
        print(f'{skaicius} x {skaiciai[1]} = {multiplied_list[1]}')
        print(f'{skaicius} x {skaiciai[2]} = {multiplied_list[2]}')
        print(f'{skaicius} x {skaiciai[3]} = {multiplied_list[3]}')
        print(f'{skaicius} x {skaiciai[4]} = {multiplied_list[4]}')
        print(f'{skaicius} x {skaiciai[5]} = {multiplied_list[5]}')
        print(f'{skaicius} x {skaiciai[6]} = {multiplied_list[6]}')
        print(f'{skaicius} x {skaiciai[7]} = {multiplied_list[7]}')
        print(f'{skaicius} x {skaiciai[8]} = {multiplied_list[8]}')
        print(f'{skaicius} x {skaiciai[9]} = {multiplied_list[9]}')
        kartojimas = input(Fore.GREEN + 'Nori kartotis kitą skaičių? (T/N)- ').lower()
        if kartojimas in kartojimas_teigiami:
            lentele()
        else:
            matematika()


matematika()
