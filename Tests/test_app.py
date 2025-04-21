import pytest
from unittest import mock
from app import Labyrinth, Pacman, Red, Pink, Blue, Orange, Game, find_direction

@pytest.fixture
def dummy_labyrinth():
    return Labyrinth("maps/first_map.txt", [0, 2], 2)

@pytest.fixture
def dummy_pacman():
    return Pacman((5, 15))

@pytest.fixture
def dummy_red():
    return Red((9, 9))

@pytest.fixture
def dummy_pink():
    return Pink((18, 19))

@pytest.fixture
def dummy_blue():
    return Blue((26, 21))

@pytest.fixture
def dummy_orange():
    return Orange((2, 30))

@pytest.fixture
def dummy_game(dummy_labyrinth, dummy_pacman, dummy_red, dummy_pink, dummy_blue, dummy_orange):
    return Game(dummy_labyrinth, dummy_pacman, dummy_red, dummy_pink, dummy_blue, dummy_orange)

@pytest.mark.parametrize("start, target, expected", [
    ((0, 0), (1, 0), 'right'),
    ((1, 0), (0, 0), 'left'),
    ((0, 1), (0, 0), 'up'),
    ((0, 0), (0, 1), 'down')
])
def test_find_direction(start, target, expected):
    assert find_direction(start, target) == expected

def test_pacman_movement(dummy_pacman):
    dummy_pacman.set_position((10, 10))
    assert dummy_pacman.get_position() == (10, 10)
    dummy_pacman.set_next_dir('right')
    assert dummy_pacman.get_next_dir() == 'right'

@pytest.mark.skip(reason="Rendering tests require display surface")
def test_render_calls():
    screen = mock.MagicMock()
    pac = Pacman((5, 5))
    pac.render(screen)
    screen.fill.assert_called()

def test_check_lose(dummy_game):
    dummy_game.pacman.set_position(dummy_game.red.get_position())
    assert dummy_game.check_lose() == True


def test_check_win(monkeypatch, dummy_game):
    monkeypatch.setattr(dummy_game.labyrinth, 'get_tile_id', lambda pos: 2)
    dummy_game.pacman.set_position((0, 0))
    assert dummy_game.check_win() is True
