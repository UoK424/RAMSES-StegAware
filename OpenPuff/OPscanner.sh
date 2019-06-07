#!/bin/bash

IFS=$'\n'
for line in $(< /tmp/tmp1); do

	echo $line | sed 's/.*(\(.*\))/\1/' >>/tmp/tmp2

done

for line in $(< /tmp/tmp2); do
printf "%d\n" $line >> /tmp/tmp3
done 
pvar=0
nvar=0
IFS=$'\n' 
for line in $(< /tmp/tmp3); do
	
	result=$(echo $line)
	if [[ $result -gt 0 ]]; then		
	pvar=$((pvar+1))
	else
	nvar=$((nvar+1))
	echo -n "" >/tmp/tmp2
	echo -n "" >/tmp/tmp3
fi
done

echo $pvar
echo $nvar

if [[ $pvar -gt $nvar ]]; then

	echo -e "OpenPuff Steganography"> ~/Desktop/Ramses/Results/OpenPuff.txt
	echo -e "yes" >> ~/Desktop/Ramses/Results/OpenPuff.txt
	echo -e "Flag Modification" >> ~/Desktop/Ramses/Results/OpenPuff.txt
	else
	echo -e "None"> ~/Desktop/Ramses/Results/OpenPuff.txt
	echo -e "None">> ~/Desktop/Ramses/Results/OpenPuff.txt
	echo -e "None">> ~/Desktop/Ramses/Results/OpenPuff.txt
	pvar=0
	nvar=0
fi 



