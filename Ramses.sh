#!/bin/bash
rm /tmp/tmp1 2> /dev/null
rm /tmp/tmp2 2> /dev/null
rm /tmp/tmp3 2> /dev/null
rm /tmp/mp4dumpfile 2> /dev/null
rm Results/Forensics.txt 2> /dev/null

LC_COLLATE=C

#filepath=~/Desktop/Ramses/TestMediaRam/*

echo -e "Welcome to RAMSES, please choose an option"
echo -e "\n 1: Video Analysis \n" "2: Image Analysis \n" "3: Metadata Forensics \n" "0: Exit \n"
read -p 'Input: ' RAMSESopt $RAMSESopt

if [ "$RAMSESopt" == "1" ]; then
clear
source RamsesVideo.sh
elif [ "$RAMSESopt" == "2" ]; then
clear
source RamsesImage.sh
elif [ "$RAMSESopt" == "3" ]; then
clear
source RamsesForensics.sh
elif [ "$RAMSESopt" == "0" ]; then
clear

#echo -n "Please give the filepath of videos for analysis: "
#read filepath $filepath
#source /home/ts424/Desktop/Ramses/Forensic.sh
#source /home/ts424/Desktop/Ramses/OpenPuff/OPStart.sh
#source /home/ts424/Desktop/Ramses/Steganosaurus/SaurusScanner.sh

function finish {
rm /tmp/tmp1 2> /dev/null
rm /tmp/tmp2 2> /dev/null
rm /tmp/tmp3 2> /dev/null
rm /tmp/mp4dumpfile 2> /dev/null
rm ~/Desktop/Ramses/Results/Forensics.txt 2> /dev/null
rm *.txt Results/ 2> /dev/null
}

trap finish EXIT 

else

exit 0
fi

cd ~/Desktop/Ramses/Results/

python convertSteg.py

cp tempStegReport.csv StegReport.csv

source ~/Desktop/Ramses/Results/mergeReport.sh

rm *.txt ~/Desktop/Ramses/Results/ 2> /dev/null
rm tempStegReport.csv Results/ 2> /dev/null

