import time
import csv


def pKnot(f, csvwriter):
    start = time.time()

    with open(f, "rb") as i:
        stream=i.read()
        if b'\xFF\xE0\x00\x10\x4A\x46\x49\x46\x00\x01\x01\x00\x00\x01' in stream:
            csvwriter.writerow([f, 'Yes', 'PixelKnot Steganography', 'ffe000104a464946000101000001'])
        else:
            csvwriter.writerow([f, 'No', 'None', ''])

    end = time.time()
    print(end - start)

