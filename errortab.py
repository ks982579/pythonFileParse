# Let this combine files together in a directory
import os
import time
import datetime

# Open Large File
resultsDir = input("Please Provide diretory of files (just name): ")
resultsDir = "./"+resultsDir

resultsList = os.listdir(resultsDir)
resultsList.sort()

# creates file name
reportTime = datetime.datetime.now()
reportTime = reportTime.strftime("%Y%m%d%H%M%S")

# Appends new file, should create if not exist



reportFileName = "./"+reportTime+".txt"
reportFile = open(reportFileName,"a")

totalFiles = len(resultsList)
fileCounter = 0

sucVar = '"isSuccessful":true'
failVar = '"isSuccessful":false'

reportFile.write("File	Success	Fail	Error\n")

# Loop through files
for eachFile in resultsList:
	sucCount = 0
	failCount = 0
	errorCount = 0
	
	currentFile = open(resultsDir+"/"+eachFile,"r")
	fileCounter += 1
	for eachLine in currentFile:
		if sucVar in eachLine:
			sucCount += 1
		elif failVar in eachLine:
			failCount += 1
		else:
			errorCount += 1
		# End If Statement Count Cycle
	# Out of For Loop for one file
	reportInfo = """{}	{}	{}	{}\n"""
		
		
	reportFile.write(reportInfo.format(eachFile,sucCount,failCount,errorCount))
	# End For eachLine
	currentFile.close()
# End For eachFile
reportFile.close()



print("Mission Complete \n closing in 3 seconds...")
time.sleep(1)
print("... 2 Seconds...")
time.sleep(1)
print("... 1 Second...")
time.sleep(1)
print("GoodBye")