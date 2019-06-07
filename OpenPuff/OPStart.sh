#!/bin/bash

rm "Results/OpenPuff.txt"

echo "${1}"

mp4file --dump "${1}" > /tmp/mp4dumpfile

grep flag /tmp/mp4dumpfile >/tmp/tmp1

source ./OpenPuff/OPscanner.sh

echo "OpenPuff Scanner" "${1}"

rm /tmp/mp4dumpfile 2> /dev/null
rm /tmp/tmp1 2> /dev/null
rm /tmp/tmp2 2> /dev/null
rm /tmp/tmp3 2> /dev/null

touch /tmp/mp4dumpfile
touch /tmp/tmp1
touch /tmp/tmp2
touch /tmp/tmp3

