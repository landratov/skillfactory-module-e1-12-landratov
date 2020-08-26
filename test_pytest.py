import pytest

from game import Game


def test_get_word():
    game = Game()
    assert game.word is not None


def test_get_current_state():
    game = Game()
    game.guessed_letters.add(game.word[0])
    state = game.get_current_state()
    assert len(state) == len(game.word)
    assert state[0] == game.word[0]
    assert '_' in state


def test_is_not_finished():
    game = Game()
    assert game.is_finished() is False


def test_is_finished():
    game = Game()
    for char in game.word:
        game.guessed_letters.add(char)
    assert game.is_finished() is True
