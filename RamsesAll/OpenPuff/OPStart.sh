#!/bin/bash
res1=$(date +%s.%N)
filenum=0

for file in $filepath
do

filenum=$((filenum+1))
mp4file --dump "${file}" > /tmp/mp4dumpfile

grep flag /tmp/mp4dumpfile >/tmp/tmp1

source /home/ts424/Desktop/Ramses/RamsesAll/OpenPuff/OPscanner.sh 

echo "OpenPuff Scanner" "${file}"
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
done


rm /tmp/mp4dumpfile 2> /dev/null
rm /tmp/tmp1 2> /dev/null
rm /tmp/tmp2 2> /dev/null
rm /tmp/tmp3 2> /dev/null

touch /tmp/mp4dumpfile
touch /tmp/tmp1
touch /tmp/tmp2
touch /tmp/tmp3
