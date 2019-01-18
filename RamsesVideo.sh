#!/bin/bash
LC_COLLATE=C
filepath=~/Desktop/Ramses/TestMediaRam/Video/*

echo -e "Video Analysis: Please choose an option"
echo -e "\n 1: Run All Scripts \n" "2: Generalised EOF \n" "3: OpenPuff Detection \n" "4: OurSecret Detection \n" "5: OmniHide Pro Detection \n" "6: BDV DataHider Detection \n" "0: Exit \n"

read -p 'Input: ' VIDopt $VIDopt

if [ "$VIDopt" == "1" ]; then
source ~/Desktop/Ramses/EOF/EOFScanner.sh
source ~/Desktop/Ramses/OpenPuff/OPStart.sh
source ~/Desktop/Ramses/OurSecret/OSScanner.sh
source ~/Desktop/Ramses/OmniHide/OHScanner.sh
source ~/Desktop/Ramses/BDV/BDVScanner.sh
#source ~/Desktop/Ramses/Steganosaurus/SaurusScanner.sh
source ~/Desktop/Ramses/RamsesForensics.sh

elif [ "$VIDopt" == "2" ]; then
source ~/Desktop/Ramses/EOF/EOFScanner.sh

source ~/Desktop/Ramses/RamsesForensics.sh

elif [ "$VIDopt" == "3" ]; then
source ~/Desktop/Ramses/OpenPuff/OPStart.sh

source ~/Desktop/Ramses/RamsesForensics.sh

elif [ "$VIDopt" == "4" ]; then
source ~/Desktop/Ramses/OurSecret/OSScanner.sh

source ~/Desktop/Ramses/RamsesForensics.sh

elif [ "$VIDopt" == "5" ]; then
source ~/Desktop/Ramses/OmniHide/OHScanner.sh

source ~/Desktop/Ramses/RamsesForensics.sh

elif [ "$VIDopt" == "6" ]; then
source ~/Desktop/Ramses/BDV/BDVScanner.sh

source ~/Desktop/Ramses/RamsesForensics.sh

#elif [ "$VIDopt" == "7" ]; then
#source ~/Desktop/Ramses/Steganosaurus/SaurusScanner.sh

source ~/Desktop/Ramses/RamsesForensics.sh

elif [ "$VIDopt" == "0" ]; then

function finish {
rm /tmp/tmp1 2> /dev/null
rm /tmp/tmp2 2> /dev/null
rm /tmp/tmp3 2> /dev/null
rm /tmp/mp4dumpfile 2> /dev/null
}

trap finish EXIT 

else

exit 0
fi
