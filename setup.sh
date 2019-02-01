#!/bin/bash

# run this when migrating to new directory
shopt -s nullglob

o="/home/darren/RAMSES_StegAware"
n=$(pwd)

for i in *.sh;
do	
	sed -i "s|$o|$n|g" "$i"
done;

for d in $(find "$n" -type d);
do
	cd
	cd "$d"
	for i in *.sh;
	do		
		sed -i "s|$o|$n|g" "$i"
	done;
done;

cd
cd "$n"

shopt -s nullglob
