import random
import time
from datetime import date
from colorama import *
import math


def pasirinkimas():
    print('|------------------------------------------|')
    print(Fore.RED + '\t|- Ką nori mokytis? ' + Fore.LIGHTBLUE_EX + '(pasirink raidę)' + Fore.RED + ' -|')
    koks_veiksmas = input(Fore.GREEN + '\tDaugybą (' + Fore.LIGHTBLUE_EX +
                          'D' + Fore.GREEN +'), \n \tDalybą (' + Fore.LIGHTBLUE_EX +
                          'B' + Fore.GREEN + '), \n \tSudėtį (' + Fore.LIGHTBLUE_EX +
                          'S' + Fore.GREEN + '), \n \tAtimtį (' + Fore.LIGHTBLUE_EX +
                          'A' + Fore.GREEN + '), \n \tkartotis daugybos lentelę (' + Fore.LIGHTBLUE_EX +
                          'L' + Fore.GREEN + '), \n \tar peržiūrėti statistiką (' + Fore.LIGHTBLUE_EX +
                          'T' + Fore.GREEN + ')?- ').lower()
    if koks_veiksmas == 'd':
        return daugyba()
    if koks_veiksmas == 'b':
        return dalyba()
    elif koks_veiksmas == 's':
        return sudetis()
    elif koks_veiksmas == 'a':
        return atimtis()
    elif koks_veiksmas == 'l':
        return lentele()
    elif koks_veiksmas == 't':
        return statistika()
    else:
        print('\tAtsakymas turi būti :' + Fore.RED + '"D", "S"' + Fore.GREEN +
              ' arba ' + Fore.RED + '"A"' + Fore.GREEN + ' raidės')
        pasirinkimas()


def daugyba():
    try:
        print(Fore.RED + '\t|- Daugybos testas -|')
        bandymai = int(input(Fore.YELLOW + '\tKelis kartus nori spręsti?' + Fore.RED +
                             ' (10/25/50)' + Fore.YELLOW + '- '))
        if bandymai in [2, 10, 25, 50]:
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
                        print(Fore.MAGENTA + 'Atsakei teisingai ' + Fore.GREEN +
                              f'{spejimai}' + Fore.MAGENTA + ' kartųus iš eilės.')
                        print(Fore.YELLOW + 'Teisingi atsakymai buvo šie:')
                        print(*atsakyti, sep="\n")
                        print('Testas išspręstas per:' + Fore.RED + f' {minutes} min. {sekundes} sek.')
                        vardas = input('Koks tavo vardas?- ')
                        f = open('statistika.txt', 'a+')
                        f.write(f'\n[{date.today()}] Vardas: {vardas}. Veiksmas: Daugyba. Atsakymai: {spejimai}. Laikas: {minutes} min. {sekundes} sek.')
                        f.close()
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
        bandymai = int(input(Fore.YELLOW + '\tKelis kartus nori spręsti?' + Fore.RED + ' (10/25/50)' + Fore.YELLOW + '- '))
        if bandymai in [2, 10, 25, 50]:
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
                        print(Fore.MAGENTA + 'Atsakei teisingai ' + Fore.GREEN +
                              f'{spejimai}' + Fore.MAGENTA + ' kartus iš eilės.')
                        print(Fore.YELLOW + 'Teisingi atsakymai buvo šie:')
                        print(*atsakyti, sep="\n")
                        print('Testas išspręstas per:' + Fore.RED + f' {minutes} min. {sekundes} sek.')
                        vardas = input('Koks tavo vardas?- ')
                        f = open('statistika.txt', 'a+')
                        f.write(f'\n[{date.today()}] Vardas: {vardas}. Veiksmas: Sudėtis. Atsakymai: {spejimai}. Laikas: {minutes} min. {sekundes} sek.')
                        f.close()
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
        bandymai = int(input(Fore.YELLOW + '\tKelis kartus nori spręsti?' + Fore.RED +
                             ' (10/25/50)' + Fore.YELLOW + '- '))
        if bandymai in [2, 10, 25, 50]:
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
                        print(Fore.MAGENTA + 'Atsakei teisingai ' + Fore.GREEN +
                              f'{spejimai}' + Fore.MAGENTA + ' kartus iš eilės.')
                        print(Fore.YELLOW + 'Teisingi atsakymai buvo šie:')
                        print(*atsakyti, sep="\n")
                        print('Testas išspręstas per:' + Fore.RED + f' {minutes} min. {sekundes} sek.')
                        vardas = input('Koks tavo vardas?- ')
                        f = open('statistika.txt', 'a+')
                        f.write(f'\n[{date.today()}] Vardas: {vardas}. Veiksmas: Atimtis. Atsakymai: {spejimai}. Laikas: {minutes} min. {sekundes} sek.')
                        f.close()
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


def dalyba():
    try:
        print(Fore.RED + '\t|- Dalybos testas -|')
        bandymai = int(input(Fore.YELLOW + '\tKelis kartus nori spręsti?' + Fore.RED +
                             ' (10/25/50)' + Fore.YELLOW + '- '))
        if bandymai in [2, 10, 25, 50]:
            pagalba = 1
            spejimai = 0
            atsakyti = []
            testo_pradzia = time.time()
            kartojimas_teigiami = ['t', 'taip', 'teip', 'y', 'yes', 'ok']

            while True:
                x = random.randint(2, 9)
                y = random.randint(2, 9)
                z = x * y
                teisinga = z / y
                teisingas = int(teisinga)
                dabar = time.time()
                uzgaista = math.ceil(dabar - testo_pradzia)
                laiko_vertimas = int(uzgaista)
                minutes = laiko_vertimas // 60
                sekundes = laiko_vertimas % 60

                print(Style.RESET_ALL)
                print('|------------------------------------------|')
                print('\tKiek bus ' + str(z) + ' / ' + str(y) + '?')
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
                    atsakyti.append([f'{x} / {y} = {teisingas}'])
                    print(Fore.GREEN + '\tPuiku! Atsakei i ' + Fore.RED + f'{spejimai}' + Fore.GREEN + ' klausymų(-us)')
                    print('\tLiko ' + Fore.RED + f'{bandymai}' + Fore.GREEN + ' klausimų(-ai)')
                    print(Style.RESET_ALL)
                    if bandymai == 0:
                        print(Fore.MAGENTA + 'Atsakei teisingai ' + Fore.GREEN +
                              f'{spejimai}' + Fore.MAGENTA + ' kartus iš eilės.')
                        print(Fore.YELLOW + 'Teisingi atsakymai buvo šie:')
                        print(*atsakyti, sep="\n")
                        print('Testas išspręstas per:' + Fore.RED + f' {minutes} min. {sekundes} sek.')
                        vardas = input('Koks tavo vardas?- ')
                        f = open('statistika.txt', 'a+')
                        f.write(f'\n[{date.today()}] Vardas: {vardas}. Veiksmas: Dalyba. Atsakymai: {spejimai}. Laikas: {minutes} min. {sekundes} sek.')
                        f.close()
                        kartojimas = input(Fore.GREEN + '\nNori bandyti dar kartą? (T/N)- ').lower()
                        if kartojimas in kartojimas_teigiami:
                            dalyba()
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
                        dalyba()
                    else:
                        pasirinkimas()
        else:
            print(
                '\tGalima rinktis iš' + Fore.RED + ' 25' + Fore.YELLOW +
                ' arba' + Fore.RED + ' 50' + Fore.YELLOW + ' spėjimų')
            dalyba()
    except ValueError:
        print('Atsakymas negali būti raidė!')
        dalyba()


def lentele():
    while True:
        kartojimas_teigiami = ['t', 'taip', 'teip', 'y', 'yes', 'ok']
        skaiciai = list(range(1, 10))
        print(Fore.BLUE + '\nPasikartosime daugybos lentelę.')
        skaicius = int(input(Fore.RED + 'Kokio skaičiaus ' + Fore.BLUE + 'daugybos lentelę norėtum pasikartoti?- '))
        sudauginti = [element * skaicius for element in skaiciai]
        print(Style.RESET_ALL)
        print(f'Daugybos lentelė iš {skaicius}')
        print(f'{skaicius} x {skaiciai[0]} = {sudauginti[0]}')
        print(f'{skaicius} x {skaiciai[1]} = {sudauginti[1]}')
        print(f'{skaicius} x {skaiciai[2]} = {sudauginti[2]}')
        print(f'{skaicius} x {skaiciai[3]} = {sudauginti[3]}')
        print(f'{skaicius} x {skaiciai[4]} = {sudauginti[4]}')
        print(f'{skaicius} x {skaiciai[5]} = {sudauginti[5]}')
        print(f'{skaicius} x {skaiciai[6]} = {sudauginti[6]}')
        print(f'{skaicius} x {skaiciai[7]} = {sudauginti[7]}')
        print(f'{skaicius} x {skaiciai[8]} = {sudauginti[8]}')
        kartojimas = input(Fore.GREEN + 'Nori kartotis kitą skaičių? (T/N)- ').lower()
        if kartojimas in kartojimas_teigiami:
            lentele()
        else:
            pasirinkimas()


def statistika():
    kartojimas_teigiami = ['t', 'taip', 'teip', 'y', 'yes', 'ok']
    with open('statistika.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            print(line)
        f.close()
    grizti = input(Fore.GREEN + 'Nori grįžti į pagrindinį meniu? (T/N)- ').lower()
    if grizti in kartojimas_teigiami:
        pasirinkimas()
    else:
        statistika()

#if __name__ = "__main__":
     #pasirinkimas()
pasirinkimas()
