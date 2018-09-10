import csv
import itertools
with open('Forensics.txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line for line in stripped if line)
    grouped = itertools.izip(*[lines] * 9)
    with open('ForensicReport.csv', 'w') as out_file:
            writer = csv.writer(out_file)
            writer.writerow(('File Name', 'File Size', 'Image Size', 'File Type Extension', 'File Access Date', 'File Modify Date', 'SHA3 512 Hash', 'Date', 'UID'))
            writer.writerows(grouped)
