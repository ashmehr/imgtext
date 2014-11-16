# placeholder for comments/info

# Function to start OCR subprocess and return recognized text
import os
import tempfile
import subprocess

def ocr (imgpath):
	tempout = tempfile.NamedTemporaryFile()

	try:
		rcode = subprocess.call(["tesseract", imgpath, tempout])
		print rcode 

		if rcode != 0:
			raise Exception
	except:
		print "OCR failed"

	with open(tempout.name + ".txt", "r") as text:
		ocrdata = text.read()

	os.remove(tempout.name + ".txt")
	os.remove(tempout.name)

	return ocrdata



