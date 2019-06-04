import re
import sys
import os
import glob
import os
import time
import csv


def ourSecret(idir, odir, s):
    count = 0
    start = time.time()
    # FileCounter = len(glob.glob('*.MP4'))

    for r, d, f in os.walk(idir):
        # count +=1
        # print(len(f))
        with open(str(odir) + '/' + str(s) + '_stegResults.csv', mode='a') as results_file:
            csvwriter = csv.writer(results_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            # csvwriter.writerow(['Filename', 'Steganography Present', 'Steganography Algorithm', 'Signature'])
            for file in f:
                # print(file)
                if '.MP4' or '.mp4' in file:
                    with open(str(idir)+'/'+str(file), "rb") as i:
                        stream=i.read()
                        if b'\x9E\x97\xBA\x2A\x00\x80\x88\xC9\xA3\x70\x97\x5B\xA2\xE4\x99\xB8\xC1\x78\x72\x0F\x88\xDD\xDC\x34\x2B\x4E\x7D\x31\x7F\xB5\xE8\x70\x39\xA8\xB8\x42\x75\x68\x71\x91' in stream:
                            csvwriter.writerow([str(file), 'Yes', 'OurSecret Steganography', '9e97ba2a008088c9a370975ba2e499b8c178720f88dddc342b4e7d317fb5e87039a8b84275687191'])
                        else:
                            csvwriter.writerow([str(file), 'No', 'None', ''])

        end = time.time()
        print(end - start)

