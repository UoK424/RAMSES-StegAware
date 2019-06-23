# Swagger API Reference: https://ramses.treelogic.com/ramses-1.0.0/swagger-ui.html#!/steganography45controller/getResultbyIdUsingGET
# Integration Guide: https://docs.google.com/document/d/1ilqehwkQdfhgymgvWMyZFWwp0jc_wfLF3CDrXCfzAlk/edit#

import stegtool_swagger_wrapper as swag
import stegtool_utils as utils
import csv
import random
import subprocess
import pyexifinfo as p
import os
import pandas as pd
import hashlib
import sys

from pathlib import Path
from main_menu import Log

from OurSecret.OurSecret import ourSecret
from Pixelknot.PixelKnot import pKnot
from BDV.BDVScanner import BDV
from OmniHide.OmniHide import omniHide


def pushResults(ui, token, usrid, results, priv, i):
	r = []

	ui.te.append('-----------------------------------\nPushing results to RAMSES platform...')
	ui.te.repaint()

	oRes = utils.local_res_parser(results, priv, i)
	exists = swag.scan_list(token, usrid)
	c = 0

	for entry in oRes:
		if any(a["image_hash"] == entry["image_hash"] for a in exists if 'image_hash' in a and 'Steganography Present' in a and entry['Steganography Present'] == 'Yes'):
			ui.te.append('\nUpdating record: ' + str(entry['id']))
			ui.te.repaint()
			ui.te.append(entry)
			ui.te.repaint()

			x = swag.update_result(token, entry, entry['id'])
			if x.status_code == 200:
				c += 1
			ui.te.append(str(x)+'\n')
			ui.te.repaint()
			r.append(x)
		elif not any(a["image_hash"] == entry["image_hash"] for a in exists if 'image_hash' in a):
		#else:
			ui.te.append('\nAdd new record: ' + str(entry['image_hash']))
			ui.te.repaint()
			x = swag.post_result(token, entry)
			if x.status_code == 200:
				c += 1
			ui.te.append(str(x)+'\n')
			r.append(x)

	ui.te.append(str(c) + ' entries pushed to the RAMSES platform\n-----------------------------------')
	ui.te.repaint()

	return r


def authenticate(usrnm, password):
	r = swag.authenticate(usrnm, password)
	return r

		
def run_tool(ui, idir, odir, v_algo, i_algo, rec):
	seshId = str(random.getrandbits(128))

	ui.te.append('-----------------------------------\nProcessing media, please wait...')
	ui.te.repaint()

	with open(str(odir) + '/' + str(seshId) + '_stegResults.csv', mode='w') as results_file:
		csvwriter = csv.writer(results_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csvwriter.writerow(['Filename', 'Steganography Present', 'Steganography Algorithm', 'Signature'])

	with open(str(odir) + '/' + str(seshId) + '_metaData.csv', mode='w') as meta_file:
		csvwriter = csv.writer(meta_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csvwriter.writerow(['Filename', 'file type', 'file size', 'file modify date', 'file access date', 'dimensions', 'sha1 Hash'])

	if rec == False:
		for r, d, f in os.walk(idir):
			for file in f:
				filename = r + '/' + file
				if str(filename).lower().endswith(('.jpg', '.jpeg', '.png', '.mp4')):
					ui.te.append('\nProcessing file: ' + str(filename))
					ui.te.repaint()
					with open(str(odir) + '/' + str(seshId) + '_stegResults.csv', mode='a') as results_file:
						csvwriter = csv.writer(results_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

						for algo in v_algo:
							if str(filename).lower().endswith('.mp4'):
								if algo == 'OurSecret':
									ourSecret(filename, file, csvwriter)
								if algo == 'BDV':
									BDV(filename, file, csvwriter)
								if algo == 'OmniHide':
									omniHide(filename, file, csvwriter)
								if algo == 'Openpuff':
									subprocess.call('echo "${}" | ./OpenPuff/OPStart.sh ' + str(filename), shell=True)

								# metadata(filename, odir, seshId)

						for algo in i_algo:
							if str(filename).lower().endswith(('.jpg', '.jpeg', '.png')):
								if algo == 'PixelKnot':
									pKnot(filename, file, csvwriter)

					metadata(filename, file, odir, seshId)

	elif rec == True:
		for filename in Path(idir).glob('**/*.*'):
			head, file = os.path.split(filename)
			if str(filename).lower().endswith(('.jpg', '.jpeg', '.png', '.mp4')):
				ui.te.append('\nProcessing file: ' + str(filename))
				ui.te.repaint()
				with open(str(odir) + '/' + str(seshId) + '_stegResults.csv', mode='a') as results_file:
					csvwriter = csv.writer(results_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
					for algo in v_algo:
						if str(filename).lower().endswith('.mp4'):
							if algo == 'OurSecret':
								ourSecret(filename, file, csvwriter)
							if algo == 'BDV':
								BDV(filename, file, csvwriter)
							if algo == 'OmniHide':
								omniHide(filename, file, csvwriter)
							if algo == 'Openpuff':
								subprocess.call('echo "${}" | ./OpenPuff/OPStart.sh ' + str(filename), shell=True)

								with open('Results/OpenPuff.txt', 'r') as oRes:
									lines = oRes.readlines()
									#print(lines)
									csvwriter.writerow([file, lines[0][:-1], lines[1][:-1], lines[2][:-1]])

							# metadata(filename, odir, seshId)

					for algo in i_algo:
						if str(filename).lower().endswith(('.jpg', '.jpeg', '.png')):
							if algo == 'PixelKnot':
								pKnot(filename, file, csvwriter)

				metadata(filename, file, odir, seshId)

	n = results_merge(odir, seshId)

	ui.te.append('\nTesting complete, please find results in ' + str(odir) + '\n-----------------------------------')
	ui.te.repaint()

	return n


def metadata(f, file, odir, seshId):
	hasher = hashlib.sha1()
	with open(f, 'rb') as ifile:
		buf = ifile.read()
		hasher.update(buf)

	with open(str(odir) + '/' + str(seshId) + '_metaData.csv', mode='a') as meta_file:
		csvwriter = csv.writer(meta_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

		m = p.get_json(f)
		csvwriter.writerow([file, m[0]['File:FileType'], m[0]['File:FileSize'], m[0]['File:FileModifyDate'], m[0]['File:FileAccessDate'], m[0]['Composite:ImageSize'], hasher.hexdigest()])

def deleteRecords(ui, token, usrid, itemlist):
	c = 0
	r = swag.scan_list(token, usrid)
	if itemlist == ['all']:
		ui.te.append('-----------------------------------\nDeleting all owned records\n')
		ui.te.repaint()
		for i in r:
			print('\n'+str(i)+'\n')
			resp = swag.delete_result(token, str(i.get('id', i)))
			if resp.status_code == 200:
				c += 1
			ui.te.append('\n' + str(resp) + ' : ' + str(i.get('id', i)))
			ui.te.repaint()
		ui.te.append('\n' + str(c) + ' entries deleted from the RAMSES platform\n-----------------------------------')
		ui.te.repaint()
	else:
		for i in itemlist:
			resp = swag.delete_result(token, str(i.get('id', i)))
			if resp.status_code == 200:
				c += 1
			ui.te.append('\n' + str(resp) + ' : ' + str(i.get('id', i)))
			ui.te.repaint()
		ui.te.append('\n' + str(c) + ' entries deleted from the RAMSES platform\n-----------------------------------')
		ui.te.repaint()


def results_merge(odir, seshId):
	mergeRes = str(odir) + '/' + str(seshId) + '_Results.csv'
	a = pd.read_csv(str(odir) + '/' + str(seshId) + '_metaData.csv')
	b = pd.read_csv(str(odir) + '/' + str(seshId) + '_stegResults.csv')
	merged = a.merge(b, on='Filename')
	merged.to_csv(mergeRes, index=False)

	return mergeRes
