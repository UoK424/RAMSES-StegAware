import re
import sys
import os
import glob
import time

count = 0
start = time.time()
FileCounter = len(glob.glob('*.MP4'))

for filename in glob.glob('*.MP4'):
    count +=1
    with open(filename, "rb") as f:
						
        stream=f.read()
        if b'\x9E\x97\xBA\x2A\x00\x80\x88\xC9\xA3\x70\x97\x5B\xA2\xE4\x99\xB8\xC1\x78\x72\x0F\x88\xDD\xDC\x34\x2B\x4E\x7D\x31\x7F\xB5\xE8\x70\x39\xA8\xB8\x42\x75\x68\x71\x91' in stream:
        
            print ("OurSecret Steganography", file = open("Results.txt",'a+'))
            print ("9e97ba2a008088c9a370975ba2e499b8c178720f88dddc342b4e7d317fb5e87039a8b84275687191", file = open("Results.txt",'a+'))
        else:
            print ("None", file = open("Results.txt",'a+'))
           
    
    print (count, "out of", FileCounter, "files processed")

    end = time.time()
    print(end - start)

