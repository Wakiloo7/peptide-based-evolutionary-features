# -*- coding: utf-8 -*-
"""ConvertFASTA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JpQymHOx2j-2Qmq8oBYyggzuZBpg5X16
"""

import sys

#File input
fileInput = open(sys.argv[1], "r")

#File output
fileOutput = open(sys.argv[2], "w")

#Seq count
count = 1 ;

#Loop through each line in the input file
#print "Converting to FASTA..."
for strLine in fileInput:

    #Strip the endline character from each input line
    strLine = strLine.rstrip("\n")

    #Output the header
    fileOutput.write(">" + str(count) + "\n")
    fileOutput.write(strLine + "\n")

    count = count + 1
print ("Done.")

#Close the input and output file
fileInput.close()
fileOutput.close()