"""Program to draw Mandelbrot fractals: the main entry point.

Author: Lars van den Haak and Tom Verhoeff

Copyright (c) 2021 - Eindhoven University of Technology, The Netherlands

This software is made available under the terms of the MIT License.
"""
from tools import *

# Don't execute this if file is imported
if __name__ == '__main__':
    entries = read_file()
    analyzer(entries)
