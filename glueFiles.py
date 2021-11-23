# Let this combine files together in a directory
import os
import time

# Open Large File
resultsDir = input("Please Provide diretory of files (just name): ")
resultsDir = "./"+resultsDir

print(resultsDir)

resultsList = os.listdir(resultsDir)
resultsList.sort()

# Appends new file, should create if not exist
bigFileName = input("What is new file's name (.json is assumed)? ")
bigFileName = "./"+bigFileName+".json"
bigFile = open(bigFileName,"a")

totalFiles = len(resultsList)
fileCounter = 0
# Loop through files
for eachFile in resultsList:
   currentFile = open(resultsDir+"/"+eachFile,"r")
   fileCounter += 1
   for eachLine in currentFile:
      if fileCounter < totalFiles: # If not the last file
         if eachLine[-1] != "\n": # If last char is not enter
            eachLine += "\n" # Add enter to line
      bigFile.write(eachLine)
   # End For eachLine
   currentFile.close()
# End For eachFile
bigFile.close()

print("Mission Complete \n closing in 3 seconds...")
time.sleep(1)
print("... 2 Seconds...")
time.sleep(1)
print("... 1 Second...")
time.sleep(1)
print("GoodBye")