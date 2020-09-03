"""The module contains a class, whose objects can be used to create ASCII art \
from an image."""


import pathlib
from PIL import Image
import numpy as np
import re
from time import time
import os


class ASCIIArt:
    """Takes an image and prints it using ASCII on the shell terminal."""

    CHAR_FACTOR = 3
    STD_HEIGHT = 300

    def __init__(self, path_to_image: str or pathlib.PosixPath = None,):
        if path_to_image is None:
            path_to_image = 'images/ascii-pineapple.jpg'

        self.path_to_image = self.valid_path(path_to_image)
        self.image = Image.open(str(self.path_to_image))
        self.arr_image = self.convert_to_array(self.image)
        self.ascii_art = None

        print(f'Image "{self.path_to_image.name}" has been successfully '
              'loaded!\n')
        print(f'Some image metadata: \
            \n- Size: {self.image.size[0]} x {self.image.size[1]} \
            \n- Format: {self.image.format} \
            \n- Mode: {self.image.mode}\n')

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
            raise FileNotFoundError(f'The path provided, does not exist. \
                                    \npath: {path}')
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

        # Resize the image to meet standard
        h = ASCIIArt.STD_HEIGHT
        ratio = image.size[0] / image.size[1]
        resized_im = image.resize((int(round(ratio * h)), h),
                                  Image.ANTIALIAS)
        return np.array(resized_im)

    @staticmethod
    def convert_to_image(array):
        """Converts a numpy array into a PIL Image class object.

        Args:
            array (np.ndarray): a 3D array that has the RGB colours of each \
                                pixel on the image.

        Raises:
            TypeError: if the argument is not a numpy array.

        Returns:
            PIL Image object: An instance of the PIL Image class.
        """
        if not type(array) == np.ndarray:
            raise TypeError('The provided argument is not a numpy array.')

        return Image.putdata(array)

    def create_brightness_matrix(self, method='luminosity'):
        """Simplifies the RGB in the array to a single value brightness value.

        Args:
            method (str): name of the method to be used to map brightness.
                          Options:
                          - average = (R + G + B) / 3
                          - lightness = (max(R,G,B) - min(R,G,B)) / 2
                          - luminosity = 0.21R + 0.72G + 0.07B

        Raises:
            ValueError: if the input method is not one of the above three.

        Returns:
            np.ndarray: a 2D array consisting of a single brightness value \
                        for each pixel.
        """
        if method not in ['average', 'lightness', 'luminosity']:
            raise ValueError(f'The input method {method} is not part of the '
                             'available ones.')

        im_arr = self.arr_image
        im_size = im_arr.shape
        b_matrix = np.ndarray(im_size[:2])

        t0 = time()
        if method == 'average':
            for row in range(im_size[0]):
                for col in range(im_size[1]):
                    b_matrix[row, col] = im_arr[row, col, :].mean()
        elif method == 'lightness':
            for row in range(im_size[0]):
                for col in range(im_size[1]):
                    num = im_arr[row, col, :].max() + \
                          im_arr[row, col, :].min()
                    b_matrix[row, col] = num / 2
        elif method == 'luminosity':
            weights = np.array([0.21, 0.72, 0.07])
            for row in range(im_size[0]):
                for col in range(im_size[1]):
                    mat = weights * im_arr[row, col, :]
                    b_matrix[row, col] = mat.sum()

        b_matrix = np.round(b_matrix)

        print(f'Time taken to create brightness matrix: '
              f'{round(time() - t0, 3)} s\n')

        return b_matrix

    def convert_to_ascii_char(self, method=0):
        """Converts the brightness matrix into a string of ASCII charaters
         that can be printed on a terminal window to create an image.

        Args:
            method (str): to be passed to create_brightness_matrix() method.

        Returns:
            str: a string of ASCII characters that when printed will create
                 the picture in terminal.
        """
        chars = "\
        `^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

        method = ['average', 'lightness', 'luminosity'][method - 1]

        b_matrix = self.create_brightness_matrix(method=method)

        minimum = b_matrix.min()
        maximum = b_matrix.max()

        def average(x, min=minimum, max=maximum, chars=chars.strip()):
            """Normalises value of x according to the min and max values.

            Args:
                x (int): value to be updated.
                min (int): minimum value in the numpy array. Defaults to 0.
                max (int): maximum value in the numpy array. Defaults to 255.

            Returns:
                int: normalised integer value of x.
            """
            value = (x - min) / (max - min) * (len(chars) - 1)
            return chars[int(round(value))] * self.CHAR_FACTOR

        ascii_scaler = average
        t0 = time()
        ascii_array = np.vectorize(ascii_scaler)(b_matrix)
        print(f'Time for ASCII conversion: {round(time() - t0, 3)} s\n')

        ascii_art = ''.join([''.join(row) for row in ascii_array.tolist()])
        self.ascii_art = ascii_art
        return ascii_art

    def print_ascii_art(self):
        height, width, RBG = self.arr_image.shape
        os.system(f"printf '\\e[8;{height};{width * self.CHAR_FACTOR}t'")
        print(self.ascii_art)


def create_ascii_art():
    """Takes user input and prints ASCII Art of the picture."""
    print('Hi! I will guide you through how you could get that picture '
          'printed in this terminal window. It is going to be made of ASCII '
          'characters!\n\nIf you get some spare time, I would love to know '
          'what you think of this project. Any kind of feedback is welcome.\n')

    print('\n* Start by going to the project folder and then "images" folder. '
          'Add any picture you would like to create art out of into this '
          'folder.')

    input('\nPress ENTER when you are done.')

    filename = input('\nEnter the name of the picture file with '
                     'its extension: ')
    art = None

    while True:
        try:
            path = pathlib.Path('images') / filename
            art = ASCIIArt(path)
            break
        except FileNotFoundError as error:
            print(error)
            filename = input('\nDid you forget to add the picture file into '
                             'the "images" folder? \n'
                             'Please re-enter a valid filename: ')
        except TypeError as error:
            print(error)
            filename = input('\nDid you forget to add the picture file into '
                             'the "images" folder? \n'
                             'Please re-enter a valid filename: ')

    method = input('Select one of the following methods to be used for '
                   'brightness mapping.\nNote: You can press ENTER to use '
                   'default.\n1. Average\n2. Lightness\n3. Luminosity\n> ')
    art.convert_to_ascii_char(method)

    print('\nPlease zoom out of terminal now. ("cmd" + "-") \n\nDETAILS: the '
          'image can be bigger than the maximum size of the current terminal '
          'window. Hence, it is better to zoom out as much as you can before '
          'the image is printed. \nREMEMBER: use "clear" command or close the '
          'window if you want to do it again.')

    input('\n\nPress ENTER when you have zoomed out enough to not read this '
          'text. * Zoom back in after typing "clear".')

    art.print_ascii_art()


if __name__ == '__main__':
    print('\nWelcome to the ASCII Art Project\n\n')
    create_ascii_art()
