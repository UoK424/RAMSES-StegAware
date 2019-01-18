#!/bin/bash

xxd -p "${file}" > /tmp/tmp1
tail -c 40 < /tmp/tmp1 | tr -d '\n' > /tmp/tmp2
if grep -q -c "0000004c61766635342e35392e313036" /tmp/tmp2; then
echo -e \ "${file}" "Signature & Atom Test - Steganosaurus content detected" >> ~/Desktop/Ramses/Results/Steganosaurus.txt
#else
#echo -e \ "${file}" "Signature & Atom Test - No Steganography found" >> ~4/Desktop/Ramses/Results/Negatives
fi

rm /tmp/tmp1 2> /dev/null
rm /tmp/tmp2 2> /dev/null

touch /tmp/tmp1
touch /tmp/tmp2

