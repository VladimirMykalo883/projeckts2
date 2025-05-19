import pytest

from main import operations_list
from src.processing import filter_by_state, sort_by_date


class Test_Filter_By_State:

    def test_filter_executed(self):
        ''' проверяет правильно ли функция отбирает по значению EXECUTED'''
        result = filter_by_state(operations_list, 'EXECUTED')
        expected = [
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {"id": 623454892, "state": "EXECUTED", "date": "2018-11-16T08:23:53.419441"},
        ]
        assert result == expected

    def test_filter_canceled(self):
        ''' проверяет правильно ли функция отбирает по значению EXECUTED'''
        result = filter_by_state(operations_list, 'CANCELED')
        expected = [
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        ]
        assert result == expected

    def test_filter_non_existent_state(self):
        ''' Проверяет, что функция возвращает пустой список, если запрашивается состояние, которого нет в operations_list.'''
        result = filter_by_state(operations_list, 'NONEXISTENT_STATE')
        expected = []
        assert result == expected

    def test_filter_empty_list(self):
        '''Проверяет, что функция возвращает пустой список, когда операции отсутствуют. '''
        result = filter_by_state([], 'EXECUTED')
        expected = []
        assert result == expected