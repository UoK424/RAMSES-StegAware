#!/bin/bash
LC_COLLATE=C
filepath=/home/darren/RAMSES_StegAware/TestMediaRam/Video/*

while true
do
	echo -e "Video Analysis: Please choose an option"
	echo -e "\n 1: Run All Scripts \n" "2: Generalised EOF \n" "3: OpenPuff Detection \n" "4: OurSecret Detection \n" "5: OmniHide Pro Detection \n" "6: BDV DataHider Detection \n" "0: Exit \n"

	read -p 'Input: ' VIDopt $VIDopt

	if [ "$VIDopt" == "1" ]; then
		source /home/darren/RAMSES_StegAware/EOF/EOFScanner.sh
		source /home/darren/RAMSES_StegAware/OpenPuff/OPStart.sh
		source /home/darren/RAMSES_StegAware/OurSecret/OSScanner.sh
		source /home/darren/RAMSES_StegAware/OmniHide/OHScanner.sh
		source /home/darren/RAMSES_StegAware/BDV/BDVScanner.sh
		#source /home/darren/RAMSES_StegAware/Steganosaurus/SaurusScanner.sh
		source /home/darren/RAMSES_StegAware/RamsesForensics.sh

	elif [ "$VIDopt" == "2" ]; then
		source /home/darren/RAMSES_StegAware/EOF/EOFScanner.sh

		source /home/darren/RAMSES_StegAware/RamsesForensics.sh
		break

	elif [ "$VIDopt" == "3" ]; then
		source /home/darren/RAMSES_StegAware/OpenPuff/OPStart.sh

		source /home/darren/RAMSES_StegAware/RamsesForensics.sh
		break

	elif [ "$VIDopt" == "4" ]; then
		source /home/darren/RAMSES_StegAware/OurSecret/OSScanner.sh

		source /home/darren/RAMSES_StegAware/RamsesForensics.sh
		break

	elif [ "$VIDopt" == "5" ]; then
		source /home/darren/RAMSES_StegAware/OmniHide/OHScanner.sh

		source /home/darren/RAMSES_StegAware/RamsesForensics.sh
		break

	elif [ "$VIDopt" == "6" ]; then
		source /home/darren/RAMSES_StegAware/BDV/BDVScanner.sh

		source /home/darren/RAMSES_StegAware/RamsesForensics.sh

		#elif [ "$VIDopt" == "7" ]; then
		#source /home/darren/RAMSES_StegAware/Steganosaurus/SaurusScanner.sh

		source /home/darren/RAMSES_StegAware/RamsesForensics.sh
		break

	elif [ "$VIDopt" == "0" ]; then

		function finish {
		rm /tmp/tmp1 2> /dev/null
		rm /tmp/tmp2 2> /dev/null
		rm /tmp/tmp3 2> /dev/null
		rm /tmp/mp4dumpfile 2> /dev/null
		}

		trap finish EXIT 
		exit 0

	else
		echo "Incorrect input, please try again."
		unset VIDopt
	fi
done
