#!/bin/bash
res1=$(date +%s.%N)
filenum=0
for file in $filepath
do
filenum=$((filenum+1))
xxd -p "${file}" > /tmp/tmp1
	tr -d '\n' < /tmp/tmp1 > /tmp/tmp2
	if grep -c -q -"9e97ba2a008088c9a370975ba2e499b8c178720f88dddc342b4e7d317fb5e87039a8b84275687191" /tmp/tmp2; then
	echo -e "OurSecret Steganography">> ~/Desktop/Ramses/Results/OurSecret.txt
	echo -e "yes" >> ~/Desktop/Ramses/Results/OurSecret.txt
	echo -e "9e97ba2a008088c9a370975ba2e499b8c178720f88dddc342b4e7d317fb5e87039a8b84275687191" >> ~/Desktop/Ramses/Results/OurSecret.txt
	else
	echo -e "None">> ~/Desktop/Ramses/Results/OurSecret.txt
	echo -e "None">> ~/Desktop/Ramses/Results/OurSecret.txt
	echo -e "None">> ~/Desktop/Ramses/Results/OurSecret.txt

fi

echo "OurSecret Scanner" "${file}"
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
done
