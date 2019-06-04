# Swagger API Reference: https://ramses.treelogic.com/ramses-1.0.0/swagger-ui.html#!/steganography45controller/getResultbyIdUsingGET
# Integration Guide: https://docs.google.com/document/d/1ilqehwkQdfhgymgvWMyZFWwp0jc_wfLF3CDrXCfzAlk/edit#

import stegtool_swagger_wrapper as swag
import stegtool_utils as utils
import json
import time
import getpass
import csv
import base64
import random
import subprocess
import pyexifinfo as p
import os
import pandas as pd
from more_itertools import unique_everseen

from OurSecret.OurSecret import ourSecret
from Pixelknot.PixelKnot import pKnot
from BDV.BDVScanner import BDV
from OmniHide.OmniHide import omniHide


def authenticate(usr,pswrd):
	token = ""
	return token

		
def run_tool(idir, odir, v_algo, i_algo):
	seshId = str(random.getrandbits(128))

	with open(str(odir) + '/' + str(seshId) + '_stegResults.csv', mode='w') as results_file:
		csvwriter = csv.writer(results_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csvwriter.writerow(['Filename', 'Steganography Present', 'Steganography Algorithm', 'Signature'])

	for algo in v_algo:
		if algo == 'OurSecret':
			ourSecret(idir, odir, seshId)
		if algo == 'BDV':
			BDV(idir, odir, seshId)
		if algo == 'OmniHide':
			omniHide(idir, odir, seshId)
	
	for algo in i_algo:
		if algo == 'pKnot':
		 	pKnot(idir, odir, seshId)

	metadata(idir, odir, seshId)
	results_merge(odir, seshId)


def metadata(idir, odir, seshId):
	metalist = []
	for r, d, f in os.walk(idir):
		for file in f:
			print(file)
			metalist.append(p.get_json(idir + '/' + file))

	with open(str(odir) + '/' + str(seshId) + '_metaData.csv', mode='w') as meta_file:
		csvwriter = csv.writer(meta_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csvwriter.writerow(['Filename', 'file type', 'file size', 'file modify date', 'file access date', 'dimensions'])

		for f in metalist:
			csvwriter.writerow([f[0]['File:FileName'], f[0]['File:FileType'], f[0]['File:FileSize'], f[0]['File:FileModifyDate'], f[0]['File:FileAccessDate'], f[0]['Composite:ImageSize']])


def results_merge(odir, seshId):
	a = pd.read_csv(str(odir) + '/' + str(seshId) + '_metaData.csv')
	b = pd.read_csv(str(odir) + '/' + str(seshId) + '_stegResults.csv')
	merged = a.merge(b, on='Filename')
	merged.to_csv(str(odir) + '/' + str(seshId) + '_Results.csv', index=False)
	# doesn't work yet, keep looking at ways to drop duplicates that do not have Steg
	df = pd.read_csv(str(odir) + '/' + str(seshId) + '_Results.csv').drop_duplicates(keep='first').reset_index()
	df.to_csv(str(odir) + '/' + str(seshId) + '_Results.csv', index=False)