#!/bin/bash
# set up script for StegAware

cd ..

sudo apt install python3-pip
sudo apt install libimage-exiftool-perl mp4v2-utils openjdk-11-jre-headless libdigest-sha3-perl
sudo -H pip3 install -r RAMSES_StegAware/requirements.txt
#sudo pip3 install PyQt5

#sudo -H pip3 install -r RAMSES_StegAware/requirements.txt
#sudo apt install libimage-exiftool-perl mp4v2-utils openjdk-11-jre-headless libdigest-sha3-perl

sudo chmod 775 -R RAMSES_StegAware/

sudo mv ~/Desktop/RAMSES_StegAware/StegAware.desktop ~/Desktop

sudo chmod 777 StegAware.desktop

cd RAMSES_StegAware/
