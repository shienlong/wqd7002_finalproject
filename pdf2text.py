"""Revisions
 26 Nov 2020; NA; Initial creation.
 22 Feb 2020; NA; edit to list files in dir. problem with saving to csv, need method.
 24 Feb 2020; 11:12pm; try to save to text and csv
"""

#extract text from PDF

import os
import pandas as pd
from pdfminer.high_level import extract_text
import csv
# from pdf2image import convert_from_path
# import cv2
# from PIL import Image
# import pytesseract
# import numpy as np
#
# cwd = os.getcwd()
#
# path = cwd + "\data"
# print(path)
#
# text = extract_text(path + '\HQ-1253 - PA.pdf')
# print(text)

path = 'C:\GitCloneDir\Final_Project\data'

files = os.listdir(path)
text = []
filecnt = 0
for f in files:
    print(f)
    text = extract_text(path + "\\" + f)
    # if f.endswith('.pdf'):
    #     filename = f[:-4]
    # with open(filename, 'w') as t:
    #     write = csv.writer(t)
    #     write.writerow(text)
    filename = path + "\\text" + "\\" + f[:-4] + '.txt'
    with open(filename, 'w', encoding="utf-8") as t:
        t.writelines(text)
        t.close()
        print('text' + str(filecnt) + ' saved...')
        filecnt += 1