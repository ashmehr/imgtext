# placeholder for comments/info
# not finding created files

# Function to start OCR subprocess and return recognized text
import os
import sys
import tempfile
import subprocess

def ocr (imgpath):
	ocrdata = ''

	try:
		tessproc = subprocess.Popen(['tesseract', imgpath, '../temp/octemp'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		tessproc.communicate()


		with open('../temp/octemp.txt', 'r') as outfile:
			ocrdata = outfile.read()

		os.remove('../temp/octemp.txt')

		
	except Exception as e:
		return 'OCR failed:'

	return ocrdata



if __name__ == '__main__':
	
	if len(sys.argv) != 2:
		print 'USAGE: python imgtext.py [PATH TO IMAGE]'

	else:
		text = ocr(sys.argv[1])

		option = raw_input( '-----WELCOME TO IMGTEXT-----\n'
		 'Select an option:\n'
		 '1. Print text to screen\n'
		 '2. Export as file\n'
		 '3. Specify custom output format\n'
		 '4. Export as PDF\n'
		 '5. Exit\n')

		sys.exit()
