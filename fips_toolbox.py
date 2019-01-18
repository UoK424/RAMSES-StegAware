import stegtool_swagger_wrapper as swag
import stegtool_utils as utils
import struct
import json
import ast
import subprocess
import csv
import numpy as np

csv.register_dialect('myDialect',delimiter=' ')
bits = []
passed = []
failed = []
mono = []
poker = []
runs = []
long_run = []
cont_run = []
xax = []

subprocess.call('./fipsscript')
print('Running FIPS 140-2 Tests over sigma data')

for i in range (0,99):
	print('Analysing sigma counters for iteration ' + str(i))
	temp_ld = []
	for j in range (1,99):
		with open('fips_sigma[0]_[0].csv'.format(i,j),'r') as f:
			rows = list(csv.reader(f))
			bits.append(rows[6][5])
			passed.append(rows[7][4])
			failed.append(rows[8][4])
			mono.append(rows[9][4])
			poker.append(rows[10][4])
			runs.append(rows[11][4])
			long_run.append(rows[12][5])
			cont_run.append(rows[13][5])

for i in range (1,100):
	xax.append(float(int(i)/100.00))

num_passed = np.array(passed)
num_failed = np.array(failed)
num_mono = np.array(mono)
num_power = np.array(poker)
num_runs = np.array(runs)
num_long_run = np.array(long_runs)
num_cont_run = np.array(cont_run)

mean_pass = np.mean(num_passed,axis=0)
mean_fail = np.mean(num_failed,axis=0)

passed_dev = np.std(num_passed,axis=0)
failed_dev = np.std(num_failed,axis=0)

fig,ax1 = plt.subplots(1)
ax1.errorbar(xax,mean_pass, passed_dev, fmt='ok', lw=1, capsize=3, label='passed tests', s=5)
ax1.set_xlabel('p')
ax1.set_ylabel('Passed')

plt.show()
