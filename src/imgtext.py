# placeholder for comments/info
# not finding created files

# Function to start OCR subprocess and return recognized text
import os
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
		return 'OCR failed:' + str(e)

	return ocrdata


