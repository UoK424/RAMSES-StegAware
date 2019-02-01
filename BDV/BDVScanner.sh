#!/bin/bash
res1=$(date +%s.%N)
filenum=0 
for file in $filepath
do
filenum=$((filenum+1))
xxd -p "${file}" > /tmp/tmp1
tr -d '\n' < /tmp/tmp1 > /tmp/tmp2
if grep -c -q "fbead881250ff9" /tmp/tmp2; 
then
echo -e "BDV Steganography">> /home/darren/RAMSES_StegAware/Results/BDV.txt
echo -e "yes" >> /home/darren/RAMSES_StegAware/Results/BDV.txt
echo -e "fbead881250ff9" >> /home/darren/RAMSES_StegAware/Results/BDV.txt
else
echo -e "None">> /home/darren/RAMSES_StegAware/Results/BDV.txt
echo -e "None">> /home/darren/RAMSES_StegAware/Results/BDV.txt
echo -e "None">> /home/darren/RAMSES_StegAware/Results/BDV.txt
fi

echo "BDV Scanner" "${file}"
echo "$filenum" "files processed"
res2=$(date +%s.%N)
dt=$(echo "$res2 - $res1" | bc)
dd=$(echo "$dt/86400" | bc)
dt2=$(echo "$dt-86400*$dd" | bc)
dh=$(echo "$dt2/3600" | bc)
dt3=$(echo "$dt2-3600*$dh" | bc)
dm=$(echo "$dt3/60" | bc)
ds=$(echo "$dt3-60*$dm" | bc)
printf "Total runtime: %d:%02d:%02d:%02.4f\n" $dd $dh $dm $ds

rm /tmp/tmp1 2> /dev/null
rm /tmp/tmp2 2> /dev/null

touch /tmp/tmp2
touch /tmp/tmp2

done
