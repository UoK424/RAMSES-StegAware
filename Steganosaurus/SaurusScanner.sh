#!/bin/bash

res1=$(date +%s.%N)
filenum=0

for file in $filepath
do

filenum=$((filenum+1))
mp4file --dump "${file}" > /tmp/mp4dumpfile
sed '6,7!d' /tmp/mp4dumpfile >/tmp/tmp1

for line in $(< /tmp/tmp1); do
echo $line | sed 's/.*(\(.*\))/\1/'>>/tmp/tmp2
done

if egrep -q "free|mdat" /tmp/tmp2; then
#source /home/ts424/Desktop/Ramses/Steganosaurus/SaurusSig.sh
echo -e \ "${file}" "Atom Test - Steganography found - running signature test"; source ~/Desktop/Ramses/Steganosaurus/SaurusSig.sh
else
echo -e \ "${file}" "Atom Test - No Steganography found" >> ~/Desktop/Ramses/Results/Negatives
fi

echo "Saurus Scanner""${file}"
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

rm /tmp/mp4dumpfile 2> /dev/null
rm /tmp/tmp1 2> /dev/null
rm /tmp/tmp2 2> /dev/null

touch /tmp/mp4dumpfile
touch /tmp/tmp1
touch /tmp/tmp2

done
