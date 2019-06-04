import re
import sys
import os
import glob
import os
import time
import csv


def pKnot(idir, odir, s):
    start = time.time()

    for r, d, f in os.walk(idir):
        with open(str(odir) + '/' + str(s) + '_stegResults.csv', mode='a') as results_file:
            csvwriter = csv.writer(results_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for file in f:
                if '.jpg' or '.JPG' or '.jpeg' or '.JPEG' or '.png' or '.PNG' in file:
                    with open(str(idir)+'/'+str(file), "rb") as i:
                        stream=i.read()
                        if b'\xFF\xE0\x00\x10\x4A\x46\x49\x46\x00\x01\x01\x00\x00\x01' in stream:
                            csvwriter.writerow([str(file), 'Yes', 'PixelKnot Steganography', 'ffe000104a464946000101000001'])
                        else:
                            csvwriter.writerow([str(file), 'No', 'None', ''])

        end = time.time()
        print(end - start)
