"""This module tests code of the-ascii-art-project"""

import pytest
from ascii_art import ASCIIArt


@pytest.fixture(scope='module')
def art():
    art = ASCIIArt()  # Create an object instance.
    return art  # 'yield' or 'return' object.
    # if 'yield', do post completion clean-up.


def test_image_loaded(art):
    assert art.image


def test_error_1():
    with pytest.raises(FileNotFoundError):
        ASCIIArt('images/i-am-not-here')


def test_error_2():
    with pytest.raises(TypeError):
        ASCIIArt('images')
