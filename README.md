# RAMSES_StegAware
Multimedia steganalysis tool developed for the RAMSES platform

RAMSES StegAware

Copyright® University of Kent, Prof. Julio Hernandez-Castro, Dr. Darren Hurley-Smith, and Thomas Sloan. This work is funded by the Horizon 2020 RAMSES project.

1.	Description
This forensic and steganalytic framework provides comprehensive analysis over image and video media and is part of the RAMSES platform. StegAware is a steganalysis tool for multimedia content (image and video) capable of detecting a diverse range of steganographic tools and techniques. The image steganalysis component of this framework uses the Java tool, StegExpose for LSB steganalysis and a series of signature detection methods. The video steganalytic feature of the tool uses signature steganalysis to cover a range of well-known video steganography tools. A feature for metadata forensics has been integrated to provide investigative details. In addition, the tool can integrate with the RAMSES platform and manage resources from its interface.

1.1	Prerequisites

The tool is available as open-source on GitHub from the following link.

https://github.com/UoK424/RAMSES_StegAware

ExifTool – The metadata forensics feature of this tool makes use of ‘ExifTool’. This is a free, open-source program for reading, writing, and manipulating file metadata. The RAMSES steganalytic tool uses these features to extract relevant metadata from video and image files. This can be installed from the following command:

$ sudo apt install libimage-exiftool-perl

Python – The reporting system is generated via python 3.X. This should be installed by default on Ubuntu distributions.   

MP4Reader – Used in the OpenPuff detection script for mp4 metadata extraction 

$ sudo apt install mp4v2-utils

File Paths – StegAware runs through a series of Bash and Python scripts. Because of this, we use relative paths to minimise setup time. The folder containing StegAware should therefore be placed on the user Desktop. If the user instead wishes to place the StegAware tool in a different directory/subdirectory, file paths can be updated across each script with the following command:

	$ Find . -name “*.sh” -exec sed -I “s/OldWord/NewWord/g” ‘{}’ \;

Java – StegExpose is a Java based tool. This installation will be required before Seek can be run. There are multiple versions that can be used. For example:

	$ sudo apt install openjdk-9-jre-headless

Dataset Path – The framework is capable of analysis for all files in a given directory. The path has to be specified in two locations. Firstly, in the RAMSES source script ‘Ramses.sh’. For example, 

filepath=/home/user/Desktop/TestVideos/*

This file path is relevant for any files that make use of the video steganalysis and image steganalysis (Pixelknot) feature. Secondly, any images analysed by ‘StegExpose’ must also have their file location specified in the ‘/StegExpose/StegExpose.sh/’ subscript. For example,

java -jar StegExpose.jar /home/user/Desktop/TestImages >> /home/user/Desktop/Ramses/Results/ImageAnalysis.txt 



*Refer to StegAware user manual for full details
