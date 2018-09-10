#!/bin/bash
res1=$(date +%s.%N)

DATE=`date '+%Y:%m:%d %H:%M:%S'`

for file in $filepath
do

if [ ${file: -4} == ".mp4" ] || [ ${file: -4} == ".MP4" ]

then 

exiftool -s -s -s -FileName -FileSize -ImageSize -FileTypeExtension -FileAccessDate -FileModifyDate -Duration "${file}" >> ~/Desktop/Ramses/Results/Forensics.txt

sha3sum -a 512 "${file}" | cut -d " " -f 1 >> ~/Desktop/Ramses/Results/Forensics.txt

echo $DATE >> ~/Desktop/Ramses/Results/Forensics.txt
date +%s | echo $RANDOM | sha512sum | head -c 32 >> ~/Desktop/Ramses/Results/Forensics.txt
echo >> ~/Desktop/Ramses/Results/Forensics.txt

cd ~/Desktop/Ramses/Results
python convertVideo.py

else


exiftool -s -s -s -FileName -FileSize -ImageSize -FileTypeExtension -FileAccessDate -FileModifyDate "${file}" >> ~/Desktop/Ramses/Results/Forensics.txt

sha3sum -a 512 "${file}" | cut -d " " -f 1 >> ~/Desktop/Ramses/Results/Forensics.txt
echo $DATE >> ~/Desktop/Ramses/Results/Forensics.txt 

date +%s | echo $RANDOM | sha512sum | head -c 32 >> ~/Desktop/Ramses/Results/Forensics.txt
echo >> ~/Desktop/Ramses/Results/Forensics.txt

cd ~/Desktop/Ramses/Results
python convertImage.py

fi

res2=$(date +%s.%N)
dt=$(echo "$res2 - $res1" | bc)
dd=$(echo "$dt/86400" | bc)
dt2=$(echo "$dt-86400*$dd" | bc)
dh=$(echo "$dt2/3600" | bc)
dt3=$(echo "$dt2-3600*$dh" | bc)
dm=$(echo "$dt3/60" | bc)
ds=$(echo "$dt3-60*$dm" | bc)



printf "Total runtime: %d:%02d:%02d:%02.4f\n" $dd $dh $dm $ds

done

rm ~/Desktop/Ramses/Results/Forensics.txt
