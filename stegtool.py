# Swagger API Reference: https://ramses.treelogic.com/ramses-1.0.0/swagger-ui.html#!/steganography45controller/getResultbyIdUsingGET
# INtegration Guide: https://docs.google.com/document/d/1ilqehwkQdfhgymgvWMyZFWwp0jc_wfLF3CDrXCfzAlk/edit#

import stegtool_swagger_wrapper as swag
import stegtool_utils as utils
import struct
import json
import ast
import subprocess
import time
import getpass

print('RAMSES Steg Tool Version 0.95 beta')

sel = 0
s = 0
s2 = 0

<<<<<<< HEAD
while True:
	usrnm = input('User Name: ')
	password = getpass.getpass('Password: ')

	temp = swag.authenticate(usrnm,password)
	access_cred = temp.content
	#print(temp.status_code)

	if (temp.status_code == 200):
		access_cred = json.loads(access_cred.decode())
		token = access_cred["access_token"]
		usrid = "986a8a37-6d96-4a04-b50d-8ef7fcc40137"
		password = ''
		break
	else:
		print("Incorrect credentials, please try again.\n")
		
=======
usrnm = input('User Name: ')
password = input('Password: ')

access_cred = swag.authenticate(usrnm,password).content
access_cred = json.loads(access_cred.decode())
token = access_cred["access_token"]
usrid = "986a8a37-6d96-4a04-b50d-8ef7fcc40137"
password = ''
>>>>>>> bfaa80a914a84dea982effbc98750fc17dbd6430

while s != '3':
	while True:
		print('\n')
		print('Menu')
		print('1. Run RAMSES Steganography Tool')
		print('2. Run RAMSES Steganography Results Handler')
		print('3. Quit RAMSES Steganography Tool')
		s = input('Selection: ')
		
		if (s == '1'):
			while s2 != 3:
				print('\n')
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
					
					c = 0
					c2 = 0
					results = utils.local_res_parser('Results/paste.csv',privacy,invest)
					exists = swag.scan_list(token,usrid)
					print('Existing records scanned')
					for i in results:
						if not any((d.get('image_hash',None) == i.get('image_hash',None)) for d in exists):
							c = c+1
							r = swag.post_result(token, i)
							print('New record: '+str(r)+' : '+str(i.get('image_hash',None)))
						elif any((d.get('image_hash',None) == i.get('image_hash',None)) for d in exists) and (i.get('steg_algorithm', None) != 'None'):
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
			while sel != 4:
				print('\n')
				print('Results Handler Menu')
				print('1. Import results from RAMSES platform')
				print('2. Submit results')
				print('3. Delete (owned) results from platform')
				print('4. Exit to top level menu')
				sel = input('Selection: ')

				if (sel == '1'):       
					r = swag.scan_list(token,usrid)
					c = utils.plat_to_csv(r)
					print(str(len(r))+' records retrieved and '+str(c)+' saved to "ramses_steg_remote.csv"')

				elif (sel == '2'):
					c = 0
					c2 = 0
					while True:
						try:
							f = input('Path of file containing update information: ')
							break
						except IOError as e:
							print(e.errno)
					
<<<<<<< HEAD
					invest = input('\nPlease input the name of the malware that your investigation is focused on (leave blank if none): ')
										
					while True:
						privacy = input('Please type public, agency or private to set the privacy level of uploaded entries: ')
						if ((privacy == 'public') or (privacy == 'private') or (privacy == 'agency')):
							break
						else:
							print('Please input a valid privacy setting.')
							
					results = utils.local_res_parser(f,privacy,invest)
					exists = swag.scan_list(token,usrid)

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

				elif (sel == '3'):
					
					c = 0
					id = input('Input file id to delete (all deletes all): ')
					if id == 'all':
						r = swag.scan_list(token,usrid)
						for i in r:
							c = c+1
							resp = swag.delete_result(token,str(i.get('id',None)))
							print(str(resp)+' : '+str(i.get('id',None)))
						print(str(c) + ' entries deleted from the RAMSES platform')

					else:
						r = swag.delete_result(str(id))
						print(str(r)+' : '+str(id))
						print('1 entry deleted from the RAMSES platform')
=======
				subprocess.call('./Ramses.sh')
				time.sleep(1)
				
				c = 0
				c2 = 0
				results = utils.local_res_parser('Results/paste.csv',privacy,invest)
				exists = swag.scan_list(token,usrid)

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
				r = swag.scan_list(token,usrid)
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
						
				results = utils.local_res_parser(f,privacy,invest)
				exists = swag.scan_list(token,usrid)

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
				
				c = 0
				id = input('Input file id to delete (all deletes all): ')
				if id == 'all':
					r = swag.scan_list(token,usrid)
					for i in r:
						c = c+1
						resp = swag.delete_result(token,str(i.get('id',None)))
						print(str(resp)+' : '+str(i.get('id',None)))
					print(str(c) + ' entries deleted from the RAMSES platform')
>>>>>>> bfaa80a914a84dea982effbc98750fc17dbd6430

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