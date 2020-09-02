"""The module contains a class, whose objects can be used to create ASCII art \
from an image."""


import pathlib
from PIL import Image
import numpy as np
import re


class ASCIIArt:
    """Takes an image and prints it using ASCII on the shell terminal."""

    def __init__(self, path_to_image: str or pathlib.PosixPath = None):
        if path_to_image is None:
            path_to_image = 'images/ascii-pineapple.jpg'

        self.path_to_image = self.valid_path(path_to_image)
        self.image = Image.open(str(self.path_to_image))
        self.arr_image = self.convert_to_array(self.image)

        print(f'Image "{self.path_to_image.name}" has been successfully \
            loaded!\n')
        print(f'Some image metadata: \
            \n- Size: {self.image.size} \
            \n- Format: {self.image.format} \
            \n- Mode: {self.image.mode}')

    @staticmethod
    def valid_path(path: str or pathlib.PosixPath):
        """The method does all the error checks to ensure an image file is present
        at the location.

        Args:
            path (str or pathlib.PosixPath): Path to the image file.

        Raises:
            TypeError: if the path input is None.
            FileNotFoundError: if the path input does not exist.
            TypeError: if the path input is not a file.

        Returns:
            pathlib.PosixPath: PosixPath object to the image file.
        """
        if path is None:
            raise TypeError('Please input a valid path to the image.')
        elif type(path) == str:
            path = pathlib.Path(path)

        if not path.exists():
            raise FileNotFoundError(f'The path provided, does not exist.\n \
                                    path: {path}')
        if not path.is_file():
            raise TypeError(f'No image file present at {path}')

        return path

    @staticmethod
    def convert_to_array(image):
        """Converts a PIL image object to a Numpy array (ndarray).

        Args:
            image (PIL Image object): An instance of the PIL Image class.

        Raises:
            TypeError: if the argument does not belong to the PIL Image class.


        Returns:
            np.ndarray: a 3D array that has the RBG colours of each pixel on \
                        the image.
        """
        pattern = r"^<class 'PIL\..+Image.+\..+Image.+'>$"
        string = str(type(image))

        if re.match(pattern, string) is None:
            raise TypeError('The provided argument is not a PIL class.')

        return np.array(image)

    @staticmethod
    def convert_to_image(array):
        """Converts a numpy array into a PIL Image class object.

        Args:
            array (np.ndarray): a 3D array that has the RBG colours of each \
                                pixel on the image.

        Raises:
            TypeError: if the argument is not a numpy array.

        Returns:
            PIL Image object: An instance of the PIL Image class.
        """
        if not type(array) == np.ndarray:
            raise TypeError('The provided argument is not a numpy array.')

        return Image.putdata(array)


if __name__ == '__main__':
    print('Welcome to the ASCII Art Project\n')
    art = ASCIIArt()
    art.image.show()
