import csv 
import json
import sys


def redirectToFile(text):
	original = sys.stdoutsys.stdout = open('tmp_txt_store.txt', 'w')
	print(text)
	sys.stdout = original


def dict_to_binary(the_dict):
    str = json.dumps(the_dict)
    binary = ' '.join(format(ord(letter), 'b') for letter in str)
    return binary


def binary_to_dict(the_binary):
    jsn = ''.join(chr(str(x, 2)) for x in the_binary.split())
    d = json.loads(jsn)  
    return d


def local_res_parser(filename,p,i):
	with open(filename,'r') as csvfile:
		reader = csv.reader(csvfile)
		next(reader)
		l_d = []
		for row in reader:
			if row[0] == '':
				print('End of records.')
				break
			else:
				if (row[1] == 'mp4'):
					d = {}
					d['date'] = row[3][:11]+row[3][11:] #row[3][:10]+"'T'"+row[3][11:]
					d['id'] = row[6]+'_'+row[0].split('/')[-1] #row[8]
					d['image_hash'] = row[6]
					d['image_type'] = row[1]
					d['privacy'] = p #make this an option!
					
					if (row[7] != 'None'):
						d['steg_algorithm'] = row[8]
						d['steg_present'] = row[7]
						d['steg_signature'] = row[9]
						d['malware_campaign'] = i
					else:
						d['steg_algorithm'] = 'None'
						d['steg_present'] = 'None'
						d['steg_signature'] = 'None'
						d['malware_campaign'] = 'None'
						
					d['duration'] = 'temp_var' # row[9]
				else:
					d = {}
					d['date'] = row[3][:11]+row[3][11:] #row[3][:10]+"'T'"+row[3][11:]
					d['id'] = row[6]+'_'+row[0].split('/')[-1] #row[]
					d['image_hash'] = row[6]
					d['image_type'] = row[1]
					d['privacy'] = p #make this an option!
					
					if (row[7] != 'None'):
						d['steg_algorithm'] = row[8]
						d['steg_present'] = row[7]
						d['steg_signature'] = row[9]
						d['malware_campaign'] = i
					else:
						d['steg_algorithm'] = 'None'
						d['steg_present'] = 'None'
						d['steg_signature'] = 'None'
						d['malware_campaign'] = 'None'
						
					d['duration'] = '00:00:00'

				l_d.append(d)
		
		return l_d


def plat_to_csv(dicts):
	c = 0
	fields=set().union(*(d.keys() for d in dicts))
	with open('Results/ramses_steg_remote.csv','w',newline='') as csvfile:
		writer = csv.DictWriter(csvfile,fields)
		writer.writeheader()
		for d in dicts:
			c = c+1
			writer.writerow(d)
	
	return c