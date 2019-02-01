#!/bin/bash
rm /tmp/tmp1 2> /dev/null
rm /tmp/tmp2 2> /dev/null
rm /tmp/tmp3 2> /dev/null
rm /tmp/mp4dumpfile 2> /dev/null
rm Results/Forensics.txt 2> /dev/null

LC_COLLATE=C

#---------------------------------------------------
#re-assigns all directory calls to this directory path
source setup.sh
#-------------------------------------------------
while true
do
	echo -e "Welcome to RAMSES, please choose an option"
	echo -e "\n 1: Video Analysis \n" "2: Image Analysis \n" "3: Metadata Forensics \n" "0: Exit \n"
	read -p 'Input: ' RAMSESopt $RAMSESopt

	if [ "$RAMSESopt" == "1" ]
	then
		unset RAMSESopt
		clear
		source RamsesVideo.sh
		break
	elif [ "$RAMSESopt" == "2" ]
	then
		unset RAMSESopt
		clear
		source RamsesImage.sh
		break
	elif [ "$RAMSESopt" == "3" ] 
	then
		unset RAMSESopt
		clear
		source RamsesForensics.sh
		break
	elif [ "$RAMSESopt" == "0" ]
	then
		unset RAMSESopt
		exit 0
	else
		unset RAMSESopt
		clear
	fi
done

function finish {
rm /tmp/tmp1 2> /dev/null
rm /tmp/tmp2 2> /dev/null
rm /tmp/tmp3 2> /dev/null
rm /tmp/mp4dumpfile 2> /dev/null
rm /home/darren/RAMSES_StegAware/Results/Forensics.txt 2> /dev/null
rm *.txt Results/ 2> /dev/null
}

trap finish EXIT 

cd /home/darren/RAMSES_StegAware/Results/

python3 convertSteg.py

cp tempStegReport.csv StegReport.csv

source /home/darren/RAMSES_StegAware/Results/mergeReport.sh

rm *.txt /home/darren/RAMSES_StegAware/Results/ 2> /dev/null
rm tempStegReport.csv Results/ 2> /dev/null
