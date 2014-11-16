# placeholder for comments/info

# Function to start OCR subprocess and return recognized text
import os
import tempfile
import subprocess

tempfile.tempdir = '../temp'

def ocr (imgpath):
	tempout = tempfile.NamedTemporaryFile(delete = False)
	ocrdata = ''

	try:
		tessproc = subprocess.Popen(['tesseract', imgpath, tempout.name], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		tessproc.communicate


		with open(tempout.name + '.txt', 'r') as outfile:
			ocrdata = outfile.read()

		os.remove(tempout.name + '.txt')
		os.remove(tempout.name)

		
	except Exception as e:
		return 'OCR failed:' + str(e)

	return ocrdata
	
	


print ocr("test.png")


