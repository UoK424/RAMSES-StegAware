import re
import sys
import os
import glob
import os
import time
import csv


def omniHide(idir, odir, s):
    start = time.time()

    for r, d, f in os.walk(idir):
        with open(str(odir) + '/' + str(s) + '_stegResults.csv', mode='a') as results_file:
            csvwriter = csv.writer(results_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for file in f:
                if '.MP4' or '.mp4' in file:
                    with open(str(idir)+'/'+str(file), "rb") as i:
                        stream=i.read()
                        count = 0
                        steg = False

                        for b in stream:
                            if b == '\x20':
                                count += 1
                                if count >= 140:
                                    csvwriter.writerow([str(file), 'Yes', 'OmniHide Steganography', 'null byte insertion'])
                                    steg = True
                                    break
                            else:
                                count = 0

                        if steg == False:
                            csvwriter.writerow([str(file), 'No', 'None', ''])

        end = time.time()
        print(end - start)

