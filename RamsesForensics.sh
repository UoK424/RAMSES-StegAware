#!/bin/bash
res1=$(date +%s.%N)

DATE=`date '+%Y:%m:%d %H:%M:%S'`

for file in $filepath
do

if [ ${file: -4} == ".mp4" ] || [ ${file: -4} == ".MP4" ]

then 

exiftool -s -s -s -FileName -FileSize -ImageSize -FileTypeExtension -FileAccessDate -FileModifyDate -Duration "${file}" >> /home/darren/RAMSES_StegAware/Results/Forensics.txt

sha3sum -a 512 "${file}" | cut -d " " -f 1 >> /home/darren/RAMSES_StegAware/Results/Forensics.txt

echo $DATE >> /home/darren/RAMSES_StegAware/Results/Forensics.txt
date +%s | echo $RANDOM | sha512sum | head -c 32 >> /home/darren/RAMSES_StegAware/Results/Forensics.txt
echo >> /home/darren/RAMSES_StegAware/Results/Forensics.txt

cd /home/darren/RAMSES_StegAware/Results
python3 convertVideo.py

else


exiftool -s -s -s -FileName -FileSize -ImageSize -FileTypeExtension -FileAccessDate -FileModifyDate "${file}" >> /home/darren/RAMSES_StegAware/Results/Forensics.txt

sha3sum -a 512 "${file}" | cut -d " " -f 1 >> /home/darren/RAMSES_StegAware/Results/Forensics.txt
echo $DATE >> /home/darren/RAMSES_StegAware/Results/Forensics.txt 

date +%s | echo $RANDOM | sha512sum | head -c 32 >> /home/darren/RAMSES_StegAware/Results/Forensics.txt
echo >> /home/darren/RAMSES_StegAware/Results/Forensics.txt

cd /home/darren/RAMSES_StegAware/Results
python3 convertImage.py

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

rm /home/darren/RAMSES_StegAware/Results/Forensics.txt
