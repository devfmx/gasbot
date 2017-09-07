#!/usr/bin/python

"""Reads barcodes.

https://pypi.python.org/pypi/pyzbar/

Before using this you need to do:

Install shared library:
$ brew install zbar

Install this:
$ pip install pyzbar Pillow
"""

from pyzbar.pyzbar import decode
from PIL import Image

def read_first_barcode(filename):
    """Reads first barcode of any type in image."""
    decoded = decode(Image.open(filename))
    if not decoded:
        raise Exception("No valid barcode found")
    return decoded[0].data

def read_cfe_barcode(filename):
    """Reads first CFE barcode in image."""
    decoded = decode(Image.open(filename))

    for match in decoded:
        # Check for right type of barcode and right length of data
        if match.type == 'CODE128' and len(match.data) == 30:
            return match.data

    raise Exception("No valid CFE barcode found")


def main():
    """Reads default image."""
    print read_cfe_barcode('barcode.png')

if __name__ == '__main__':
    main()
