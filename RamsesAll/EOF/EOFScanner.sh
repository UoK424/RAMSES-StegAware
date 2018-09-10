#!/bin/bash

catch1="FindIntegerProperty: no such property"
catch2="invalid atom size, extends outside parent atom"

mp4file --dump "${file}" > /tmp/tmp1
filenum=$((filenum+1))

test=$(grep -o "invalid atom size, extends outside parent atom" /tmp/tmp1)
echo $test >/tmp/tmp2

if [[ $test == $catch2 ]]
then
test=$(grep -o "FindIntegerProperty: no such property" /tmp/tmp1)
echo $test >/tmp/tmp2
if [[ $test == $catch1 ]]
then
trap finish EXIT 
else
echo -e \ "${file}" "EOF Test - EOF injection detected! Running signature tests" >>/home/ts424/Desktop/Ramses/Results/EOFInjection.txt; source /home/ts424/Desktop/Ramses/RamsesAll/OurSecret/OSScanner.sh

fi
fi

echo "EOF Scanner" "${file}"
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

touch /tmp/tmp1
touch /tmp/tmp2
