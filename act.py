#!/usr/local/bin/python3.7
# -*- coding:utf-8 -*-
import pytesseract
from PIL import Image

if __name__ == '__main__':
    im = Image.open(r'/Users/edz/Documents/3.png')
    string = pytesseract.image_to_string(im, lang='chi_sim')
    print(string)