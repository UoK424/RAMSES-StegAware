import time
import csv


def BDV(f, csvwriter):
    start = time.time()

    with open(f, "rb") as i:
        stream = i.read()
        if b'\xfb\xea\xd8\x81\x25\x0f\xf9' in stream:
            csvwriter.writerow([f, 'Yes', 'BDV Steganography', 'fbead881250ff9'])
        else:
            csvwriter.writerow([f, 'No', 'None', ''])

    end = time.time()
    print(end - start)
