# tests/test_game.py
from longest_word.game import Game
import string

class TestGame:
    def test_game_initialization(self):
            # setup
            new_game = Game()

            # exercise
            grid = new_game.grid

            # verify
            assert isinstance(grid, list)
            assert len(grid) == 9
            for letter in grid:
                assert letter in string.ascii_uppercase

def test_no_word_is_invalid(self):
    # setup
    new_game = Game()

    # exercice

    # verify
    assert new_game.is_valid('') is False

def word_is_valid(self):
    # setup
    new_game = Game()
    solution='nine'

    # exercice
    new_game.grid = ['n', 'i', 'n', 'e', 'c', 'a', 'r', 'a', 'c']

    # verify
    assert new_game.is_valid(solution) is True

def word_is_invalid(self):
    # setup
    new_game = Game()
    solution='zero'

    # exercice
    new_game.grid = ['n', 'i', 'n', 'e', 'c', 'a', 'r', 'a', 'c']

    # verify
    assert new_game.is_valid(solution) is False
