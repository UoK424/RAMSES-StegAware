#!/bin/bash
filepath=$1
odir=$2

for file in $filepath
do

if [ ${file: -4} == ".mp4" ] || [ ${file: -4} == ".MP4" ]

then 

exiftool -s -s -s -FileName -FileSize -ImageSize -FileTypeExtension -FileAccessDate -FileModifyDate -Duration "${file}" >> odir + /Forensics.txt

sha3sum -a 512 "${file}" | cut -d " " -f 1 >> odir + /Forensics.txt

#echo $DATE >> ~/Desktop/Ramses/Results/Forensics.txt

date +%s | echo $RANDOM | sha512sum | head -c 32 >> odir + /Forensics.txt
echo >> odir + /Forensics.txt

# cd ~/Desktop/Ramses/Results
# python3 convertVideo.py

elif [ ${file: -4} == ".jpeg" ] || [ ${file: -4} == ".jpg" ] || [ ${file: -4} == ".JPEG" ] || [ ${file: -4} == ".png" ] || [ ${file: -4} == ".PNG" ] 

exiftool -s -s -s -FileName -FileSize -ImageSize -FileTypeExtension -FileAccessDate -FileModifyDate "${file}" >> odir + /Forensics.txt

sha3sum -a 512 "${file}" | cut -d " " -f 1 >> odir + /Forensics.txt

#echo $DATE >> ~/Desktop/Ramses/Results/Forensics.txt 

date +%s | echo $RANDOM | sha512sum | head -c 32 >> odir + /Forensics.txt
echo >> odir + /Forensics.txt

# cd ~/Desktop/Ramses/Results
# python3 convertImage.py

fi

done

rm ~/Desktop/Ramses/Results/Forensics.txt
