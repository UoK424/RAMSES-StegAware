#!/bin/bash

filenum=$((filenum+1))
xxd -p "${file}" > /tmp/tmp1
tr -d '\n' < /tmp/tmp1 > /tmp/tmp2
tac /tmp/tmp2 > /tmp/tmp3
if grep -q -E -m1 \(20\)\{140,\} /tmp/tmp3; then
echo -e \ "Signature test - OmniHide signature found" "${file}" >> /home/ts424/Desktop/Ramses/Results/OmniHidePro.txt
else
echo -e \ "OmniHide Pro - No Steganography Detected" "${file}" >> /home/ts424/Desktop/Ramses/Results/Negatives 
fi

echo "OmniHide Scanner" "${file}"
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
rm /tmp/tmp3 2> /dev/null

touch /tmp/tmp1
touch /tmp/tmp2
touch /tmp/tmp3

#source /home/ts424/Desktop/Ramses/Steganosaurus/SaurusScanner.sh

