import time
import csv


def omniHide(f, csvwriter):
    start = time.time()
    with open(f, "rb") as i:
        stream = i.read()
        steg = False

        for b in stream:
            if b == '\x20':
                count += 1
                if count >= 140:
                    csvwriter.writerow([f, 'Yes', 'OmniHide Steganography', 'null byte insertion'])
                    steg = True
                    break
                else:
                    count = 0

        if steg == False:
            csvwriter.writerow([f, 'No', 'None', ''])

    end = time.time()
    print(end - start)

    return steg

