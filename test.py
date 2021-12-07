"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""

from main import *


def test_create_level():
    assert isinstance(create_level(), str)


def test_create_levels_list():
    assert isinstance(create_levels_list(), list)


def test_floor_to_list():
    assert isinstance(floor_to_list("xxxxxxxxxxxxxxxxxxxxxxxxx"), list)
    assert floor_to_list("xxxxxxxxxxxxxxxxxxxxxxxxx") == ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x",
                                                          "x", "x", "x", "x", "x", "x", "x", "x", "x", "x",
                                                          "x", "x", "x", "x", "x", ]


def test_list_to_floor():
    assert isinstance(list_to_floor(["x", "x", "x", "x", "x", "x", "x", "x", "x", "x",
                                     "x", "x", "x", "x", "x", "x", "x", "x", "x", "x",
                                     "x", "x", "x", "x", "x", ]), list)
    assert list_to_floor(["x", "x", "x", "x", "x", "x", "x", "x", "x", "x",
                          "x", "x", "x", "x", "x", "x", "x", "x", "x", "x",
                          "x", "x", "x", "x", "x", ]) == "xxxxxxxxxxxxxxxxxxxxxxxxx"
