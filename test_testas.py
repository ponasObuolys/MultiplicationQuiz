import pytest
from testas import MathQuiz, Operacija

def test_skaiciuoti():
    quiz = MathQuiz()
    assert quiz.skaiciuoti(5, 3, '+') == 8
    assert quiz.skaiciuoti(5, 3, '-') == 2
    assert quiz.skaiciuoti(5, 3, '*') == 15
    assert quiz.skaiciuoti(6, 2, '/') == 3

def test_gauti_laika():
    quiz = MathQuiz()
    quiz.testo_pradzia = 0
    minutes, sekundes = quiz.gauti_laika()
    assert isinstance(minutes, int)
    assert isinstance(sekundes, int)
    assert sekundes >= 0 and sekundes < 60

def test_operaciju_reiksmes():
    assert Operacija.DAUGYBA.value[0] == '*'
    assert Operacija.DALYBA.value[0] == '/'
    assert Operacija.SUDETIS.value[0] == '+'
    assert Operacija.ATIMTIS.value[0] == '-'

def test_bandymu_validacija():
    quiz = MathQuiz()
    assert 10 in quiz.GALIMI_BANDYMAI
    assert 25 in quiz.GALIMI_BANDYMAI
    assert 50 in quiz.GALIMI_BANDYMAI
    assert 100 not in quiz.GALIMI_BANDYMAI 