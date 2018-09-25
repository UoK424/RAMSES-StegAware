import stegtool_swagger_wrapper as swag
import stegtool_utils as utils
import struct
import json
import ast
import subprocess
import time

print('RAMSES Steg Tool Version 0.9 beta')

sel = 0
s = 0
s2 = 0

while s != '3':
	print('\n')
	print('Menu')
	print('1. Run RAMSES Steganography Tool')
	print('2. Run RAMSES Steganography Results Handler')
	print('3. Quit RAMSES Steganography Tool')
	s = input('Selection: ')
	
	while True:
		print('\n')
		if (s == '1'):
			print('Steganography Tool Menu')
			print('1. Run tool and push results to RAMSES platform')
			print('2. Run tool locally')
			print('3. Exit to top level menu')
			s2 = input('Selection: ')
			
			if (s2 == '1'):
				print('Tool runs here with push to server')
				invest = input('\nPlease input the name of the malware that your investigation is focused on (leave blank if none): ')
				while True:
					privacy = input('Please type public, agency or private to set the privacy level of uploaded entries: ')
					if ((privacy == 'public') or (privacy == 'private') or (privacy == 'agency')):
						break
					else:
						print('Please input a valid privacy setting.')
					
				subprocess.call('./Ramses.sh')
				time.sleep(1)
				
				usrnm = input('User Name: ')
				password = input('Password: ')

				access_cred = swag.authenticate(usrnm,password).content
				#print(access_cred)
				access_cred = json.loads(access_cred.decode())
				token = access_cred["access_token"]
				password = ''
				#print(token)
				
				c = 0
				c2 = 0
				results = utils.local_res_parser('Results/paste.csv',privacy,invest)
				exists = swag.scan_list(token)

				print('Existing records scanned')

				for i in results:
					if not any((d.get('image_hash',None) == i.get('image_hash',None)) for d in exists):
						c = c+1
						r = swag.post_result(token, i)
						print('New record: '+str(r)+' : '+str(i.get('image_hash',None)))
					elif any((d.get('image_hash',None) == i.get('image_hash',None)) for d in exists) and (i.get('steg_algorithm', None) != 'None'):
						#print(i.get('steg_algorithm',None))
						c2 = c2+1
						r = swag.update_result(token, i, str(i.get('id',None)))
						print('Updated '+str(r)+' : '+str(i.get('image_hash',None)))
					else:
						print('Duplicate record not updated.')

				print(str(c) + ' unique new entries and ' + str(c2) + ' updates pushed to RAMSES platform')
				
			elif (s2 == '2'):
				print('Tool runs here without push to server')
				subprocess.call('./Ramses.sh')
				
			elif (s2 == '3'):
				print('Exiting to top level menu.')
				break
				
			else:
				print('Incorrect selection, please try again.')
			
		elif (s == '2'): 			
			print('Results Handler Menu')
			print('1. Import results from RAMSES platform')
			#print('2. Get result by id')
			print('2. Submit results')
			#print('4. Update result')
			print('3. Delete (owned) results from platform')
			print('4. Exit to top level menu')
			sel = input('Selection: ')

			if (sel == '1'):       
				usrnm = input('User Name: ')
				password = input('Password: ')

				access_cred = swag.authenticate(usrnm,password).content
				#print(access_cred)
				access_cred = json.loads(access_cred.decode())
				token = access_cred["access_token"]
				password = ''
				#print(token)

				r = swag.scan_list(token)
				c = utils.plat_to_csv(r)
				print(str(len(r))+' records retrieved and '+str(c)+' saved to "ramses_steg_remote.csv"')

			#elif (sel == '2'):
				#i = input('Input file id to recall: ')
				#r = swag.get_result(token,i).content
				#print(r.content)
				#c = utils.plat_to_csv(r)
				#print(str(len(r))+' records retrieved and '+str(c)+' saved to "/Results/ramses_steg_remote.csv"')

			elif (sel == '2'):
				c = 0
				c2 = 0
				while True:
					try:
						f = input('Path of file containing update information: ')
						break
					except IOError as e:
						print(e.errno)
				
				invest = input('\nPlease input the name of the malware that your investigation is focused on (leave blank if none): ')
									
				while True:
					privacy = input('Please type public, agency or private to set the privacy level of uploaded entries: ')
					if ((privacy == 'public') or (privacy == 'private') or (privacy == 'agency')):
						break
					else:
						print('Please input a valid privacy setting.')
						
				usrnm = input('User Name: ')
				password = input('Password: ')

				access_cred = swag.authenticate(usrnm,password).content
				#print(access_cred)
				access_cred = json.loads(access_cred.decode())
				token = access_cred["access_token"]
				password = ''
				#print(token)
						
				results = utils.local_res_parser(f,privacy,invest)
				exists = swag.scan_list(token)

				print('Existing records scanned')

				for i in results:
					if not any((d.get('image_hash',None) == i.get('image_hash',None)) for d in exists):
						c = c+1
						r = swag.post_result(token, i)
						print('New record: '+str(r)+' : '+str(i.get('image_hash',None)))
					elif any((d.get('image_hash',None) == i.get('image_hash',None)) for d in exists) and (i.get('steg_algorithm', None) != 'None'):
						c2= c2+1
						r = swag.update_result(token, i, str(i.get('id',None)))
						print('Updated '+str(r)+' : '+str(i.get('image_hash',None)))
					else:
						print('Duplicate record not updated.')

				print(str(c) + ' unique new entries and ' + str(c2) + ' updates pushed to RAMSES platform')

#			elif (sel == '4'):
#				i = input('Input file id to update (all updates all locally held entries to platform): ')
#				while True:
#					try:
#						f = input('Name of file containing update information: ')
#						break
#					except IOError as e:
#						print(e.errno)
#						
#				results = utils.local_res_parser(f)
#
#				if i == 'all':
#					for j in results:
#						resp = swag.update_result(token,j,i)
#						print(resp)
#
#				else:
#					result = next((item for item in results if item['id'] == i), None)
#					resp = swag.update_result(token, result, i).content
#					print(resp)

			elif (sel == '3'):
				usrnm = input('User Name: ')
				password = input('Password: ')

				access_cred = swag.authenticate(usrnm,password).content
				#print(access_cred)
				access_cred = json.loads(access_cred.decode())
				token = access_cred["access_token"]
				password = ''
				#print(token)
				
				c = 0
				id = input('Input file id to delete (all deletes all): ')
				if id == 'all':
					r = swag.scan_list(token)
					for i in r:
						c = c+1
						resp = swag.delete_result(token,str(i.get('id',None)))
						print(str(resp)+' : '+str(i.get('id',None)))
					print(str(c) + ' entries deleted from the RAMSES platform')

				else:
					r = swag.delete_result(str(id))
					print(str(r)+' : '+str(id))
					print('1 entry deleted from the RAMSES platform')

			elif (sel == '4'):
				print('Exiting to top level menu')
				break
			else:
				print('Incorrect command, please try again or quit')
				
				
		elif (s == '3'): 
			print('Exiting program.')
			break
		else:
			print('Incorrect selection, please try again.')
