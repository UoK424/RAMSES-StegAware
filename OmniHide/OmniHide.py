import time
import csv


def omniHide(f, csvwriter):
    start = time.time()
    with open(f, "rb") as i:
        stream = i.read()
        steg = False
        bstring = ''

        for i in range(0, 140):
            bstring = bstring + '\x20'

        print(bstring)
        
        if bstring.encode('utf-8') in stream:
            csvwriter.writerow([f, 'Yes', 'OmniHide Steganography', 'null byte insertion'])
        else:
            csvwriter.writerow([f, 'No', 'None', ''])

    end = time.time()
    print(end - start)

