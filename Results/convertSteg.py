import os
import os.path
import csv
import itertools
import glob

temp_rows = []

for filename in glob.glob('*.txt'):
	with open(filename, 'r') as in_file:

		stripped = tuple(line.strip() for line in in_file)
		lines = (line for line in stripped if line)
		grouped = list(itertools.izip(*[lines] * 3))
			
		if os.path.isfile('tempStegReport.csv'):
			#print('Yes file')
			
			with open('tempStegReport.csv', 'r') as in_file:
				reader = csv.reader(in_file,delimiter=',')
				temp_rows = []
				for row in reader:
					if row[0] != 'Steg_Algorithm':
						temp_rows.append(row)

			with open('tempStegReport.csv', 'w') as out_file:
				writer = csv.writer(out_file)
				writer.writerow(('Steg_Algorithm', 'Steg_Present', 'Steg_Signature'))
				if len(temp_rows) > 0:
					#print('Yes rows')
					for i in range (0,len(temp_rows)):
						if temp_rows[i][0] != 'None':
							#print('Line from temp')
							writer.writerow(temp_rows[i])
						#elif temp_rows[i][0] != 'EOF Steganography':
							#print('Line from temp 2')
							#writer.writerow(temp_rows[i])
						else:
							#print('Line from file')
							writer.writerow(grouped[i])
				else:
					print('No rows')
					writer.writerows(grouped)
					
		else:
			#print('No file')
			with open('tempStegReport.csv', 'w') as out_file:
				writer = csv.writer(out_file)
				writer.writerow(('Steg_Algorithm', 'Steg_Present', 'Steg_Signature'))
				writer.writerows(grouped)

