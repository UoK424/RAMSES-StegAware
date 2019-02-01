#!/bin/bash
filepath=/home/darren/RAMSES_StegAware/TestMediaRam/Image/*
res1=$(date +%s.%N)

while true
do
	echo -e "Image Analysis: Please choose an option"
	echo -e "\n 1: Run all \n" "2: StegExpose (LSB) \n" "3: Pixelknot (F5) \n" "0: Exit \n"
	
	read -p 'Input: ' IMAGEopt $IMAGEopt

	if [ "$IMAGEopt" == "1" ]; then
		source /home/darren/RAMSES_StegAware/Pixelknot/PKScanner.sh
		source /home/darren/RAMSES_StegAware/StegExpose/StegExpose.sh
		source /home/darren/RAMSES_StegAware/RamsesForensics.sh
	break

	elif [ "$IMAGEopt" == "2" ]; then
		source /home/darren/RAMSES_StegAware/StegExpose/StegExpose.sh

		source /home/darren/RAMSES_StegAware/RamsesForensics.sh
	break

	elif [ "$IMAGEopt" == "3" ]; then
		source /home/darren/RAMSES_StegAware/Pixelknot/PKScanner.sh

		source /home/darren/RAMSES_StegAware/RamsesForensics.sh
	break

	elif [ "$IMAGEopt" == "0" ]; then

		function finish {
		rm /tmp/tmp1 2> /dev/null
		rm /tmp/tmp2 2> /dev/null
		rm /tmp/tmp3 2> /dev/null
		rm /tmp/mp4dumpfile 2> /dev/null
		}

		trap finish EXIT 
		exit 0

	else	
		echo "Invalid input, please try again."
		unset IMAGEopt
	fi
done

rm /home/darren/RAMSES_StegAware/Results/Negatives 2> /dev/null
