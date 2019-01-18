#!/bin/bash
filepath=~/Desktop/Ramses/TestMediaRam/Image/*
res1=$(date +%s.%N)

while true
do
	echo -e "Image Analysis: Please choose an option"
	echo -e "\n 1: Run all \n" "2: StegExpose (LSB) \n" "3: Pixelknot (F5) \n" "0: Exit \n"
	
	read -p 'Input: ' IMAGEopt $IMAGEopt

	if [ "$IMAGEopt" == "1" ]; then
		source ~/Desktop/Ramses/Pixelknot/PKScanner.sh
		source ~/Desktop/Ramses/StegExpose/StegExpose.sh
		source ~/Desktop/Ramses/RamsesForensics.sh
	break

	elif [ "$IMAGEopt" == "2" ]; then
		source ~/Desktop/Ramses/StegExpose/StegExpose.sh

		source ~/Desktop/Ramses/RamsesForensics.sh
	break

	elif [ "$IMAGEopt" == "3" ]; then
		source ~/Desktop/Ramses/Pixelknot/PKScanner.sh

		source ~/Desktop/Ramses/RamsesForensics.sh
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

rm ~/Desktop/Ramses/Results/Negatives 2> /dev/null
