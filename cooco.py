#!/usr/bin/env python
''''''''''''''''''''''''''''''''''''''''''''''
'                   CooCo                    '
'############################################'
'             By: Duncan Murdock             '
'                 Version: 1                 '
'              Date: 01/12/2014              '
'--------------------------------------------'
' Converts files between CooRecorder output  '
' (Cybis DENDRO) and COFECHA input (Tucson). '
'''''''''''''''''''''''''''''''''''''''''''''
import csv
import argparse

stopMarker = "-9999" # depends on measurements
cooFile = None
coFile = None
numbers = ['1','2','3','4','5','6','7','8','9','0']

def readCooFile(f,name=None):
	cooBuffer = []
	outBuffer = []
	try:
		f = open(f, "r")
	except(IOException):
		print "File not found!"
	readIn = f.readline()
	while readIn:
		cooBuffer.append(readIn.strip())
		readIn = f.readline()
	cooBuffer = filter(lambda x: x[0] in numbers, cooBuffer)
	for item in cooBuffer:
		splitBuffer = item.split(',')[1]
		splitBuffer = splitBuffer.split('.')[1]
		outBuffer.append(splitBuffer)
	outBuffer.append(stopMarker)
	outBuffer.insert(0,'0')
	if name:
		outBuffer.insert(0,name)
	else:
		outBuffer.insert(0,f.name.split('.')[0][-7:])
	return outBuffer

def writeCoFile(cooData,name="output.txt"): #name then 10 measurement cols as per Tucson standard
	with open(name,"wb") as f:
		f = csv.writer(f, delimiter=" ")
		for item in cooData:
			itemname = item[0]
			item = item[1::]
			recWriter(item,itemname,f)

def recWriter(item,name,f): #recursive department of recursion
	fileBuffer = []
	length = len(item)
	if length <= 10:
		fileBuffer.append(name)
		fileBuffer.extend(item)
		f.writerow(fileBuffer)
		return
	else:
		fileBuffer.append(name)
		fileBuffer.extend(item[:9:])
		f.writerow(fileBuffer)
		recWriter(item[10::],name,f)

def main():
	filelist = []
	parser = argparse.ArgumentParser(prog="CooCo",description="Converts CooRecorder output for COFECHA")
	parser.add_argument("file", action="append", help="File or folder of files to convert.")
	parser.add_argument("-o","--output", help="The output file. Default is ./output.txt.")
	args = parser.parse_args()
	files = args.file
	filelist = []
	for item in files:
		try:
			filelist.extend(os.listdir(args.file))
		except:
			if type(args.file) is list:
				filelist.extend(args.file)
			else:
				filelist.append(args.file)
	writeBuffer = []
	for item in filelist:
		writeBuffer.append(readCooFile(item))
	if args.output:
		writeCoFile(writeBuffer,args.output)
	else:
		writeCoFile(writeBuffer)
	print "Finished!"

if __name__ == "__main__":
	main()