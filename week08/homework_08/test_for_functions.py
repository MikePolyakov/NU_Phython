"""
тесты функций консольного файлового менеджера и программы викторина
"""
from filemanager import author_info
from victory import date_to_str
from main import is_correct_choice
from all_functions import separator
from all_functions import data_reading
import os


# тест для функции чтения баланса из файла при отсутствии файла
def test_data_reading():
    if not os.path.exists('balance.txt'):
        assert data_reading('balance.txt', 'int') == 0


def test_is_correct_choice():
    assert is_correct_choice('1') == 1
    assert is_correct_choice('0') == 0
    assert is_correct_choice('6') == 1
    assert is_correct_choice('OO') == 0


def test_separator():
    assert separator(3) == '***'


def test_author_info():
    assert author_info() == 'PUBLIC DOMAIN ⓒ2019'


def test_date_to_str():
    assert date_to_str('01.01.2020') == 'первое января 2020 года'
