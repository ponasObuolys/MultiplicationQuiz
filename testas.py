import random
import time
from colorama import *
import math


def pasirinkimas():
    print('|------------------------------------------|')
    print(Fore.RED + '\t|- Ką šiandien nori mokytis? -|')
    koks_veiksmas = input(Fore.GREEN + '\tDaugybą (' + Fore.RED + 'D' + Fore.GREEN +
                          '), Sudėtį (' + Fore.RED + 'S' + Fore.GREEN + '), Atimtį (' + Fore.RED +
                          'A' + Fore.GREEN + ') ar kartotis daugybos lentelę (' + Fore.RED +
                          'L' + Fore.GREEN + ')?- ').lower()
    if koks_veiksmas == 'd':
        return daugyba()
    elif koks_veiksmas == 's':
        return sudetis()
    elif koks_veiksmas == 'a':
        return atimtis()
    elif koks_veiksmas == 'l':
        return lentele()
    else:
        print('\tAtsakymas turi būti :' + Fore.RED + '"D", "S"' + Fore.GREEN +
              ' arba ' + Fore.RED + '"A"' + Fore.GREEN + ' raidės')
        pasirinkimas()


def daugyba():
    try:
        print(Fore.RED + '\t|- Daugybos testas -|')
        bandymai = int(input(Fore.YELLOW + '\tKelis kartus nori spręsti?' + Fore.RED +
                             ' (25/50)' + Fore.YELLOW + '- '))
        if bandymai in [2, 25, 50]:
            print(Style.RESET_ALL)
            pagalba = 1
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
                laiko_vertimas = int(uzgaista)
                minutes = laiko_vertimas // 60
                sekundes = laiko_vertimas % 60

                print(Style.RESET_ALL)
                print('|------------------------------------------|')
                print('\tKiek bus ' + str(x) + ' x ' + str(y) + '?')
                if pagalba == 1:
                    print(Fore.BLUE + '\tPaspaudus NULĮ (0) galėsi vieną karta pasinaudoti pagalba')
                else:
                    pass
                atsakimas = int(input(Fore.BLUE + '\tĮrašyk atsakymą ir paspausk ENTER:- '))
                print('|------------------------------------------|')
                if atsakimas == 0 and pagalba == 1:
                    ar_pagalba = input(Fore.GREEN + '\tAr tikrai nori pasinaudoti pagalba? (T/N)- ')
                    if ar_pagalba in kartojimas_teigiami:
                        pagalba -= 1
                        print(f'\tTeisingas atsakymas yra: ' + Fore.RED + f'{teisingas}')
                    else:
                        continue
                elif atsakimas == 0 and pagalba == 0:
                    print('\tPagalba išnaudota')
                elif atsakimas == teisingas:
                    bandymai -= 1
                    spejimai += 1
                    atsakyti.append([f'{x} x {y} = {teisingas}'])
                    print(Fore.GREEN + '\tPuiku! Atsakei i ' + Fore.RED + f'{spejimai}' + Fore.GREEN + ' klausymų(-us)')
                    print('\tLiko ' + Fore.RED + f'{bandymai}' + Fore.GREEN + ' klausimų(-ai)')
                    print(Style.RESET_ALL)
                    if bandymai == 0:
                        print('Testas išspręstas per:' + Fore.RED + f' {minutes} min. {sekundes} sek.')
                        print(Fore.MAGENTA + 'Atsakei teisingai ' + Fore.GREEN +
                              f'{spejimai}' + Fore.MAGENTA + 'kartų(-us) iš eilės.')
                        print(Fore.YELLOW + 'Teisingi atsakymai buvo šie:')
                        print(*atsakyti, sep="\n")
                        kartojimas = input(Fore.GREEN + '\nNori bandyti dar kartą? (T/N)- ').lower()
                        if kartojimas in kartojimas_teigiami:
                            daugyba()
                        else:
                            pasirinkimas()
                    else:
                        pass
                else:
                    print('\nNETEISINGAI! ' + Fore.RED + 'Teisingas atsakymas: ' + Fore.GREEN + '{}'.format(teisingas))
                    print(Fore.RED + 'Atsakei teisingai ' + Fore.GREEN +
                          f'{spejimai}' + Fore.RED + ' kartą(-us) iš eilės.')
                    if spejimai > 0:
                        print(Fore.YELLOW + 'Teisingi atsakymai buvo šie:')
                        print(*atsakyti, sep="\n")
                        print('\nTestas neišspręstas. Užtrukai:' + Fore.RED + f' {minutes} minutes. {sekundes} sek.')
                        print(Style.RESET_ALL)
                    else:
                        pass
                    kartojimas = input(Fore.GREEN + 'Nori bandyti dar kartą? (T/N)- ').lower()
                    if kartojimas in kartojimas_teigiami:
                        daugyba()
                    else:
                        pasirinkimas()
        else:
            print(
                '\tGalima rinktis iš' + Fore.RED + ' 25' + Fore.YELLOW +
                ' arba' + Fore.RED + ' 50' + Fore.YELLOW + ' spėjimų')
            daugyba()
    except ValueError:
        print('Atsakymas negali būti raidė!')
        daugyba()


def sudetis():
    try:
        print(Fore.RED + '\t|- Sudėties testas -|')
        bandymai = int(input(Fore.YELLOW + '\tKelis kartus nori spręsti?' + Fore.RED + ' (25/50)' + Fore.YELLOW + '- '))
        if bandymai in [2, 25, 50]:
            print(Style.RESET_ALL)
            pagalba = 1
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
                laiko_vertimas = int(uzgaista)
                minutes = laiko_vertimas // 60
                sekundes = laiko_vertimas % 60

                print(Style.RESET_ALL)
                print('|------------------------------------------|')
                print('\tKiek bus ' + str(x) + ' + ' + str(y) + '?')
                if pagalba == 1:
                    print(Fore.BLUE + '\tPaspaudus NULĮ (0) galėsi vieną karta pasinaudoti pagalba')
                else:
                    pass
                atsakimas = int(input(Fore.BLUE + '\tĮrašyk atsakymą ir paspausk ENTER:- '))
                print('|------------------------------------------|')
                if atsakimas == 0 and pagalba == 1:
                    ar_pagalba = input(Fore.GREEN + '\tAr tikrai nori pasinaudoti pagalba? (T/N)- ')
                    if ar_pagalba in kartojimas_teigiami:
                        pagalba -= 1
                        print(f'\tTeisingas atsakymas yra: ' + Fore.RED + f'{teisingas}')
                    else:
                        continue
                elif atsakimas == 0 and pagalba == 0:
                    print('\tPagalba išnaudota')
                elif atsakimas == teisingas:
                    bandymai -= 1
                    spejimai += 1
                    atsakyti.append([f'{x} + {y} = {teisingas}'])
                    print(Fore.GREEN + '\tPuiku! Atsakei i ' + Fore.RED + f'{spejimai}' + Fore.GREEN + ' klausymų(-us)')
                    print('\tLiko ' + Fore.RED + f'{bandymai}' + Fore.GREEN + ' klausimų(-ai)')
                    print(Style.RESET_ALL)
                    if bandymai == 0:
                        print('Testas išspręstas per:' + Fore.RED + f' {minutes} min. {sekundes} sek.')
                        print(Fore.MAGENTA + 'Atsakei teisingai ' + Fore.GREEN +
                              f'{spejimai}' + Fore.MAGENTA + 'kartų(-us) iš eilės.')
                        print(Fore.YELLOW + 'Teisingi atsakymai buvo šie:')
                        print(*atsakyti, sep="\n")
                        kartojimas = input(Fore.GREEN + '\nNori bandyti dar kartą? (T/N)- ').lower()
                        if kartojimas in kartojimas_teigiami:
                            sudetis()
                        else:
                            pasirinkimas()
                    else:
                        pass
                else:
                    print('\nNETEISINGAI! ' + Fore.RED + 'Teisingas atsakymas: ' + Fore.GREEN + '{}'.format(teisingas))
                    print(Fore.RED + 'Atsakei teisingai ' + Fore.GREEN +
                          f'{spejimai}' + Fore.RED + ' kartą(-us) iš eilės.')
                    if spejimai > 0:
                        print(Fore.YELLOW + 'Teisingi atsakymai buvo šie:')
                        print(*atsakyti, sep="\n")
                        print('\nTestas neišspręstas. Užtrukai:' + Fore.RED + f' {minutes} minutes. {sekundes} sek.')
                        print(Style.RESET_ALL)
                    else:
                        pass
                    kartojimas = input(Fore.GREEN + 'Nori bandyti dar kartą? (T/N)- ').lower()
                    if kartojimas in kartojimas_teigiami:
                        sudetis()
                    else:
                        pasirinkimas()
        else:
            print(
                '\tGalima rinktis iš' + Fore.RED + ' 25' + Fore.YELLOW +
                ' arba' + Fore.RED + ' 50' + Fore.YELLOW + ' spėjimų')
            sudetis()
    except ValueError:
        print('Atsakymas negali būti raidė!')
        sudetis()


def atimtis():
    try:
        print(Fore.RED + '\t|- Atimties testas -|')
        bandymai = int(input(Fore.YELLOW + '\tKelis kartus nori spręsti?' + Fore.RED + ' (25/50)' + Fore.YELLOW + '- '))
        if bandymai in [2, 25, 50]:
            print(Style.RESET_ALL)
            pagalba = 1
            spejimai = 0
            atsakyti = []
            testo_pradzia = time.time()
            kartojimas_teigiami = ['t', 'taip', 'teip', 'y', 'yes', 'ok']

            while True:
                x = random.randint(89, 199)
                y = random.randint(11, 88)
                teisingas = x - y
                dabar = time.time()
                uzgaista = math.ceil(dabar - testo_pradzia)
                laiko_vertimas = int(uzgaista)
                minutes = laiko_vertimas // 60
                sekundes = laiko_vertimas % 60

                print(Style.RESET_ALL)
                print('|------------------------------------------|')
                print('\tKiek bus ' + str(x) + ' - ' + str(y) + '?')
                if pagalba == 1:
                    print(Fore.BLUE + '\tPaspaudus NULĮ (0) galėsi vieną karta pasinaudoti pagalba')
                else:
                    pass
                atsakimas = int(input(Fore.BLUE + '\tĮrašyk atsakymą ir paspausk ENTER:- '))
                print('|------------------------------------------|')
                if atsakimas == 0 and pagalba == 1:
                    ar_pagalba = input(Fore.GREEN + '\tAr tikrai nori pasinaudoti pagalba? (T/N)- ')
                    if ar_pagalba in kartojimas_teigiami:
                        pagalba -= 1
                        print(f'\tTeisingas atsakymas yra: ' + Fore.RED + f'{teisingas}')
                    else:
                        continue
                elif atsakimas == 0 and pagalba == 0:
                    print('\tPagalba išnaudota')
                elif atsakimas == teisingas:
                    bandymai -= 1
                    spejimai += 1
                    atsakyti.append([f'{x} - {y} = {teisingas}'])
                    print(Fore.GREEN + '\tPuiku! Atsakei i ' + Fore.RED + f'{spejimai}' + Fore.GREEN + ' klausymų(-us)')
                    print('\tLiko ' + Fore.RED + f'{bandymai}' + Fore.GREEN + ' klausimų(-ai)')
                    print(Style.RESET_ALL)
                    if bandymai == 0:
                        print('Testas išspręstas per:' + Fore.RED + f' {minutes} min. {sekundes} sek.')
                        print(Fore.MAGENTA + 'Atsakei teisingai ' + Fore.GREEN +
                              f'{spejimai}' + Fore.MAGENTA + 'kartų(-us) iš eilės.')
                        print(Fore.YELLOW + 'Teisingi atsakymai buvo šie:')
                        print(*atsakyti, sep="\n")
                        kartojimas = input(Fore.GREEN + '\nNori bandyti dar kartą? (T/N)- ').lower()
                        if kartojimas in kartojimas_teigiami:
                            atimtis()
                        else:
                            pasirinkimas()
                    else:
                        pass
                else:
                    print('\nNETEISINGAI! ' + Fore.RED + 'Teisingas atsakymas: ' + Fore.GREEN + '{}'.format(teisingas))
                    print(Fore.RED + 'Atsakei teisingai ' + Fore.GREEN +
                          f'{spejimai}' + Fore.RED + ' kartą(-us) iš eilės.')
                    if spejimai > 0:
                        print(Fore.YELLOW + 'Teisingi atsakymai buvo šie:')
                        print(*atsakyti, sep="\n")
                        print('\nTestas neišspręstas. Užtrukai:' + Fore.RED + f' {minutes} minutes. {sekundes} sek.')
                        print(Style.RESET_ALL)
                    else:
                        pass
                    kartojimas = input(Fore.GREEN + 'Nori bandyti dar kartą? (T/N)- ').lower()
                    if kartojimas in kartojimas_teigiami:
                        atimtis()
                    else:
                        pasirinkimas()
        else:
            print(
                '\tGalima rinktis iš' + Fore.RED + ' 25' + Fore.YELLOW +
                ' arba' + Fore.RED + ' 50' + Fore.YELLOW + ' spėjimų')
            atimtis()
    except ValueError:
        print('Atsakymas negali būti raidė!')
        atimtis()


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
        kartojimas = input(Fore.GREEN + 'Nori kartotis kitą skaičių? (T/N)- ').lower()
        if kartojimas in kartojimas_teigiami:
            lentele()
        else:
            pasirinkimas()


#if __name__ = "__main__":
     #pasirinkimas()
pasirinkimas()
