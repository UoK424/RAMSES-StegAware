~!/bin/bash
# set up script for StegAware

cd ..

pip3 install -r requirements.txt
apt install libimage-exiftool-perl mp4v2-utils openjdk-11-jre-headless libdigest-sha3-perl
chmod 755 -R RAMSES_StegAware/

cd RAMSES_StegAware/