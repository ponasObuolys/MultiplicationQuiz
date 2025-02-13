import random
import time
from datetime import date
from rich.console import Console
from rich.theme import Theme
import math
from enum import Enum
from typing import List, Tuple
import json
from pathlib import Path

custom_theme = Theme({
    "error": "red",
    "success": "green",
    "info": "blue"
})

console = Console(theme=custom_theme)

class Operacija(Enum):
    DAUGYBA = ('*', 'Daugybos', (2, 9), (2, 9))
    DALYBA = ('/', 'Dalybos', (2, 9), (2, 9))
    SUDETIS = ('+', 'Sudėties', (11, 99), (11, 99))
    ATIMTIS = ('-', 'Atimties', (89, 199), (11, 88))


class TextFormatter:
    @staticmethod
    def klaida(tekstas: str) -> None:
        console.print(tekstas, style="error")

    @staticmethod
    def sekme(tekstas: str) -> None:
        console.print(tekstas, style="success")

    @staticmethod
    def info(tekstas: str) -> None:
        console.print(tekstas, style="info")


class MathQuiz:
    KARTOJIMAS_TEIGIAMI = ['t', 'taip', 'teip', 'y', 'yes', 'ok']
    GALIMI_BANDYMAI = [10, 25, 50]

    def __init__(self):
        self.pagalba = 1
        self.spejimai = 0
        self.atsakyti = []
        self.testo_pradzia = 0
        self.formatter = TextFormatter()

    def gauti_laika(self) -> Tuple[int, int]:
        dabar = time.time()
        uzgaista = math.ceil(dabar - self.testo_pradzia)
        minutes = uzgaista // 60
        sekundes = uzgaista % 60
        return minutes, sekundes

    def saugoti_statistika(self, vardas: str, veiksmas: str, spejimai: int, minutes: int, sekundes: int):
        statistika = {
            'data': str(date.today()),
            'vardas': vardas,
            'veiksmas': veiksmas,
            'atsakymai': spejimai,
            'laikas': f"{minutes} min. {sekundes} sek."
        }
        
        with open('statistika.txt', 'a+', encoding='utf-8') as f:
            f.write(f"\n[{statistika['data']}] Vardas: {statistika['vardas']}. "
                   f"Veiksmas: {statistika['veiksmas']}. "
                   f"Atsakymai: {statistika['atsakymai']}. "
                   f"Laikas: {statistika['laikas']}")

    def rodyti_progresa(self, bandymai: int, spejimai: int):
        console.print(f'\tPuiku! Atsakei į {spejimai} klausimų(-us)')
        console.print(f'\tLiko {bandymai} klausimų(-ai)')

    def vykdyti_testa(self, operacija: Operacija) -> None:
        try:
            console.print(f'\t|- {operacija.value[1]} testas -|')
            bandymai = self.gauti_bandymu_skaiciu()
            
            if bandymai not in self.GALIMI_BANDYMAI:
                console.print(f'\tGalima rinktis iš {self.GALIMI_BANDYMAI} spėjimų')
                return self.vykdyti_testa(operacija)

            self.testo_pradzia = time.time()
            while bandymai > 0:
                x = random.randint(*operacija.value[2])
                y = random.randint(*operacija.value[3])
                
                if operacija == Operacija.DALYBA:
                    teisingas = x
                    x = x * y
                else:
                    teisingas = self.skaiciuoti(x, y, operacija.value[0])

                if not self.speti_atsakyma(x, y, teisingas, operacija.value[0], bandymai):
                    break
                bandymai -= 1

        except ValueError:
            console.print('Atsakymas turi būti skaičius!')
            self.vykdyti_testa(operacija)

    def skaiciuoti(self, x: int, y: int, operatorius: str) -> int:
        if operatorius == '+': return x + y
        if operatorius == '-': return x - y
        if operatorius == '*': return x * y
        if operatorius == '/': return x // y
        raise ValueError(f"Nežinomas operatorius: {operatorius}")

    def gauti_bandymu_skaiciu(self) -> int:
        return int(input(console.print('\tKelis kartus nori spręsti? (10/25/50) - ')))

    def speti_atsakyma(self, x: int, y: int, teisingas: int, operatorius: str, bandymai: int) -> bool:
        console.print('\n|------------------------------------------|')
        console.print(f'\tKiek bus {x} {operatorius} {y}?')
        
        if self.pagalba == 1:
            console.print('\tPaspaudus NULĮ (0) galėsi vieną kartą pasinaudoti pagalba')

        atsakymas = int(input(console.print('\tĮrašyk atsakymą ir paspausk ENTER: ')))

        if atsakymas == 0 and self.pagalba == 1:
            return self.naudoti_pagalba(teisingas)
        elif atsakymas == 0 and self.pagalba == 0:
            console.print('\tPagalba jau išnaudota')
            return True
        elif atsakymas == teisingas:
            self.spejimai += 1
            self.atsakyti.append(f'{x} {operatorius} {y} = {teisingas}')
            self.rodyti_progresa(bandymai - 1, self.spejimai)
            
            if bandymai == 1:
                self.baigti_testa(True)
            return True
        else:
            console.print(f'\nNETEISINGAI! Teisingas atsakymas: {teisingas}')
            self.baigti_testa(False)
            return False

    def naudoti_pagalba(self, teisingas: int) -> bool:
        if input(console.print('\tAr tikrai nori pasinaudoti pagalba? (T/N) ')).lower() in self.KARTOJIMAS_TEIGIAMI:
            self.pagalba -= 1
            console.print(f'\tTeisingas atsakymas yra: {console.print(str(teisingas))}')
            return True
        return True

    def baigti_testa(self, sekme: bool):
        minutes, sekundes = self.gauti_laika()
        if sekme:
            console.print(f'Atsakei teisingai {self.spejimai} kartus iš eilės.')
        else:
            console.print(f'Atsakei teisingai {self.spejimai} kartą(-us) iš eilės.')
        
        if self.spejimai > 0:
            console.print('Teisingi atsakymai buvo šie:')
            console.print(*self.atsakyti, sep="\n")
        
        laiko_tekstas = f'{minutes} min. {sekundes} sek.'
        console.print(f'{"Testas išspręstas" if sekme else "Testas neišspręstas"} per: {console.print(laiko_tekstas)}')
        
        if sekme:
            vardas = input('Koks tavo vardas? ')
            self.saugoti_statistika(vardas, "Matematika", self.spejimai, minutes, sekundes)

def rodyti_statistika():
    try:
        with open('statistika.txt', 'r', encoding='utf-8') as f:
            console.print('\n\tStatistika:')
            console.print(f.read())
    except FileNotFoundError:
        console.print('\tStatistikos failas dar neegzistuoja.')

def pagrindinis_meniu():
    while True:
        console.print('|------------------------------------------|')
        TextFormatter.klaida('\t|- Ką nori mokytis? ')
        TextFormatter.info('(pasirink raidę) ')
        TextFormatter.klaida('-|')
        
        pasirinkimas = input(
            TextFormatter.sekme(
                '\tDaugybą (D), \n' +
                '\tDalybą (B), \n' +
                '\tSudėtį (S), \n' +
                '\tAtimtį (A), \n' +
                '\tPeržiūrėti statistiką (T)? '
            )
        ).lower()

        quiz = MathQuiz()
        
        if pasirinkimas == 'd':
            quiz.vykdyti_testa(Operacija.DAUGYBA)
        elif pasirinkimas == 'b':
            quiz.vykdyti_testa(Operacija.DALYBA)
        elif pasirinkimas == 's':
            quiz.vykdyti_testa(Operacija.SUDETIS)
        elif pasirinkimas == 'a':
            quiz.vykdyti_testa(Operacija.ATIMTIS)
        elif pasirinkimas == 't':
            rodyti_statistika()
        else:
            console.print(TextFormatter.klaida('\tNeteisingas pasirinkimas. Bandykite dar kartą.'))

if __name__ == '__main__':
    pagrindinis_meniu()
