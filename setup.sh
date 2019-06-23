#!/bin/bash
# set up script for StegAware

cd ..

sudo -H pip3 install -r RAMSES_StegAware/requirements.txt
sudo apt install libimage-exiftool-perl mp4v2-utils openjdk-11-jre-headless libdigest-sha3-perl

sudo -H pip3 install -r RAMSES_StegAware/requirements.txt
sudo apt install libimage-exiftool-perl mp4v2-utils openjdk-11-jre-headless libdigest-sha3-perl

sudo chmod 755 -R RAMSES_StegAware/

cd RAMSES_StegAware/
