import os
import csv
import itertools
import glob

for filename in glob.glob('*.txt'):
	with open(filename, 'r') as in_file:

    		stripped = (line.strip() for line in in_file)
    		lines = (line for line in stripped if line)
    		grouped = itertools.izip(*[lines] * 3)
    		with open('StegReport.csv', 'w') as out_file:
            		writer = csv.writer(out_file)
            		writer.writerow(('Steg_Algorithm', 'Steg_Present', 'Steg_Signature'))
	                writer.writerows(grouped)

