"""
Файл в котором тестируются все функции
"""
from utils import *
import pytest


@pytest.mark.parametrize("a, expected_result", [("ф", [30]),
                                                ("а", [33]),
                                                ("паф", [34, 33, 30])])
def test_convert_to_numbers(a, expected_result):
    temp = a
    assert convert_to_numbers(temp) == expected_result


@pytest.mark.parametrize("a, expected_result", [([42], {'lfi5': 2, 'lfi4': 0, 'lfi3': 0, 'lfi2': 0, 'rfi2': 0, 'rfi\
3': 0, 'rfi4': 0, 'rfi5': 0}),
                                                ([42, 35, 33, 46, 19, 54, 48, 21, 18, 49, 31], {'lfi5': 2, 'lfi4': 0, '\
lfi3': 3, 'lfi2': 4, 'rfi2': 4, 'rfi3': 0, 'rfi4': 0, 'rfi5': 2})])
def test_count_of_move(a, expected_result):
    assert count_of_move(a) == expected_result


@pytest.mark.parametrize("a, expected_result", [(['РаскИнуты рУки, горЯт глазА\n', 'Мы стАли оскОлками наАшего прОшлог\
о'], ['РаскИнуты', 'рУки,', 'горЯт', 'глазАE', 'Мы', 'стАли', 'оскОлками', 'наАшего', 'прОшлогоE'])])
def test_read_word(a, expected_result):
    assert read_word(a) == expected_result
    
