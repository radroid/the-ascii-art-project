"""This module tests code of the-ascii-art-project"""

import pytest
import the_ascii_art_project


@pytest.fixture(scope='module')
def instance():
    # Create an object instance.
    return False  # 'yield' or 'return' object.
    # if 'yield', do post completion clean-up.


def test_(instance):
    assert not instance  # Simple assert test


def test_error_1():
    with pytest.raises(UserWarning):
        raise UserWarning  # Error raised test
