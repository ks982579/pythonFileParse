# Let this File split
import os
import time

# Open Large File
rawFileName = input("Please Provide File Name (exclude .json): ")
fileExt = input("provide file extension (exclude dot): ")
maxFileSize = int(input("Max File Size: "))
relFileName = "./"+rawFileName+"."+fileExt

# Reads file. Error and Crash if not exist
bigFile = open(relFileName,"r")

# Make new directory to store parts
# Consider Try/catch
os.mkdir("./parts")

# create file to save lines into
newFileNames = rawFileName+"p"
fileNumber = 1

lineCount = maxFileSize
# reading in the bigfile
for linex in bigFile:
    if lineCount == maxFileSize:
        #if line count is max, create a new file...
        # New numext
        # new file
        try:
            tempFile.close()
        except:
            print("No file Open")
            
        numext = str(fileNumber)
        if len(numext) == 1:
            numext = "00"+numext
        elif len(numext) == 2:
            numext = "0"+numext
        tempFileName = newFileNames+numext+"."+fileExt
        tempFile = open("./parts/"+tempFileName,"a")
        lineCount = 0
        fileNumber+=1
    ## End If ##

    # Remove Trailing "new line" if last line for file
    if lineCount == (maxFileSize -1):
        linex = linex.replace("\n","")

    #Write Line to file
    tempFile.write(linex)

    lineCount+=1
# End For

tempFile.close()
print("Mission Complete \n closing in 3 seconds...")
time.sleep(1)
print("... 2 Seconds...")
time.sleep(1)
print("... 1 Second...")
time.sleep(1)
print("GoodBye")
