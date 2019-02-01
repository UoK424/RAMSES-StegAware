#!/bin/bash

cd /home/darren/RAMSES_StegAware/StegExpose/

java -jar StegExpose.jar /home/darren/RAMSES_StegAware/TestMediaRam/Image >> /home/darren/RAMSES_StegAware/Results/ImageAnalysis.txt

res2=$(date +%s.%N)
dt=$(echo "$res2 - $res1" | bc)
dd=$(echo "$dt/86400" | bc)
dt2=$(echo "$dt-86400*$dd" | bc)
dh=$(echo "$dt2/3600" | bc)
dt3=$(echo "$dt2-3600*$dh" | bc)
dm=$(echo "$dt3/60" | bc)
ds=$(echo "$dt3-60*$dm" | bc)

printf "Total runtime: %d:%02d:%02d:%02.4f\n" $dd $dh $dm $ds
