# RAMSES_StegAware
Multimedia steganalysis tool developed for the RAMSES platform

RAMSES StegAware

Copyright® University of Kent, Prof. Julio Hernandez-Castro, Dr. Darren Hurley-Smith, and Thomas Sloan. This work is funded by the Horizon 2020 RAMSES project.

Description
This forensic and steganalytic framework provides comprehensive analysis over image and video media and is part of the RAMSES platform. StegAware is a steganalysis tool for multimedia content (image and video) capable of detecting a diverse range of steganographic tools and techniques. The image steganalysis component of this framework uses the Java tool, StegExpose for LSB steganalysis and a series of signature detection methods. The video steganalytic feature of the tool uses signature steganalysis to cover a range of well-known video steganography tools. A feature for metadata forensics has been integrated to provide investigative details. In addition, the tool can integrate with the RAMSES platform and manage resources from its interface.

Quick Start Guide

The following steps can be used for a quick setup of the tool. 


1.0	$cd Desktop  
1.1	$git clone https://github.com/UoK424/RAMSES_StegAware.git  
1.2 $sudo apt install python3-pip
1.3	$sudo chmod -R 755 <Directory>
1.4 $cd <Directory>
1.5 $sudo bash ./setup.sh
1.6	Run the tool with $sudo python3 main_menu.py

If the setup.sh script doesn't work (or program has unmet dependencies after completion of that script), refer to the manual for set-by-step setup.  




*Refer to StegAware user manual for full details of the tool's setup and use.
