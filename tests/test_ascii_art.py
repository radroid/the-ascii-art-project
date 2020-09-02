"""This module tests code of the-ascii-art-project"""

import pytest
from ascii_art import ASCIIArt
import numpy


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


def test_convert_to_array_type(art):
    assert type(art.arr_image) == numpy.ndarray


def test_convert_to_array_shape(art):
    expected_shape = art.image.size[1], art.image.size[0], \
        len(art.image.format) - 1
    assert art.arr_image.shape == expected_shape


def test_convert_to_array_error(art):
    with pytest.raises(TypeError):
        art.convert_to_array('Hello')


def test_convert_to_array_error_2(art):
    with pytest.raises(TypeError):
        art.convert_to_array(art)


def test_brightness_matrix_size(art):
    b_mat = art.create_brightness_matrix()
    im_size = art.image.size[::-1]
    assert b_mat.shape == im_size
