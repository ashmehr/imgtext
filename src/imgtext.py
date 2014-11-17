# placeholder for comments/info
# not finding created files

# Function to start OCR subprocess and return recognized text
from PyPDF2 import PdfFileWriter
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
			outfile.close()
		os.remove('../temp/octemp.txt')

		
	except Exception as e:
		return 'OCR failed:' + str(e)

	return ocrdata

def printText(text):
	print text

def exportFile(text):
	filename = raw_input('Enter filename\n')

	if '.pdf' in filename:
		return 'Invalid filename! Export as PDF instead'

	path = raw_input('Enter path to save file to\n')

	try :
		with open(path + '/' + filename, 'w+') as outfile:
			outfile.write(text)
			outfile.close()

		print 'File ' + filename +' created successfully in ' + path + '\n'

	except Exception as e:
		print 'File creation failed: ' + str(e)

def exportPDF(text):
	outputPDF = PdfFileWriter()
	filename = raw_input('Enter filename\n')
	path = raw_input('Enter path to save PDF to\n')
	outputFile = file(path + '/' + filename, 'wb')
	outputPDF.write(outputFile)

if __name__ == '__main__':
	
	if len(sys.argv) != 2:
		print 'USAGE: python imgtext.py [PATH TO IMAGE]'

	else:
		text = ocr(sys.argv[1])
		while True:
			option = raw_input( '-----WELCOME TO IMGTEXT-----\n'
								'Select an option:\n'
								'1. Print text to screen\n'
								'2. Export as file\n'
								'3. Export as PDF\n'
								'4. Exit\n')

			if option == '1':
				printText(text)
			elif option == '2':
				exportFile(text)
			elif option == '3':
				print 'Work in progress!\n'
			elif option == '4':
				print 'Thanks for using imgText!\n'
				sys.exit()
			else:
				print 'Invalid option\n'





