'''
Convert a folder of Microsoft Word Docs into pdf 
'''
import sys, os
import win32com.client
import logging 
import logging.handlers
import re
import argparse
import time

DEFAULT_LOG_FORMAT = "%(asctime)s - %(name)-20s - %(message)s"
LOG_LEVELS = ("debug", "info")

def process_files(directory):
	logger = logging.getLogger("Converting Word and Ppt")
	newlist = []
	if os.path.isdir(directory):
		for path, dirs, files in os.walk(directory):
			for f in files:
				if f.endswith(".docx") or f.endswith(".doc") or f.endswith('pptx'):
					newlist.append([path, dirs, f])
					logger.debug("File added to the list to be converted: {}\r".format(f)) 
				else:
					logger.debug("Incorrect File Type: {}\r".format(f)) 

	return newlist

def word_to_pdf(newlist, directory, output):
	failed_files = []
	for file_name_1 in newlist:
		file_name = file_name_1[0]
		for a in file_name_1:
			if a:
				file_name = os.path.join(file_name, a)

		file = file_name_1[-1]
		file_ = ''.join(file.split('.')[:-1])

		logger.debug("Processing File {}\r".format(file_name))
		try:
			if file_name.split('.')[-1] == 'docx' or file_name.split('.')[-1] == 'doc':
				word = win32com.client.Dispatch('Word.Application')
				wdFormatPDF = 17
				doc = word.Documents.Open(file_name)
				word.Visible = False
				file_name = file_name.split('.')[0]
				doc.SaveAs(output + "\\" + file_ + ".pdf", FileFormat=wdFormatPDF)
				doc.Close()
				word.Quit()
				logger.info("successfully converted {}\r".format(file_))
				time.sleep(5)

			
			elif file_name.split('.')[-1] == 'pptx':
				powerpoint = win32com.client.Dispatch('Powerpoint.Application')
				ppt_file_format = 32
				doc = powerpoint.Presentations.Open(file_name)
				powerpoint.Visible = False
				file_name = file_name.split('.')[0]
				doc.SaveAs(output  +"\\" + file_ + ".pdf", FileFormat=ppt_file_format)
				doc.Close()
				powerpoint.Quit()
				logger.info("successfully converted {}\r".format(file_))
				time.sleep(5)
			
		except:
			if doc:
				doc.Close()
			failed_files.append(file_name)
			logger.info("Failed to convert {}\r".format(file_))
			time.sleep(5)
			continue

if __name__ == '__main__':
	parser = argparse.ArgumentParser(
        description='Convert Word To Pdf'
    )
	parser.add_argument('-d','--debug',
                        help='Print lots of debugging statements',
                        action="store_const",dest="loglevel",const=logging.DEBUG,
                        default=logging.INFO
                    )
	parser.add_argument('-f', '--folder', help='Path to folder')
	parser.add_argument('-o', '--output', help='Save pdf to output folder')
	args = parser.parse_args()

	logger = logging.getLogger(__name__)
	FORMAT = '%(asctime)s - %(module)-16s - %(levelname)s - %(message)s'
	logging.basicConfig(level=args.loglevel, format=FORMAT)

	if not args.output: 
		cwd = os.getcwd()
	else:
		if os.path.exists(args.output) == False:
			if args.output.split('/')[0] == ".":
				cwd = os.getcwd()
				path = re.sub(r'^./', '', args.output)
				cwd = os.path.join(cwd, path)
				if not os.path.exists(cwd):
					os.mkdir(cwd)
			else:
				os.mkdir(args.output) 
				cwd = args.output
		else:
			cwd = args.output

	folder = args.folder
	if folder.split('/')[0] == ".":
		wd = os.getcwd()
		path = re.sub(r'.', '', folder)
		folder = os.path.join(wd, path)

	word_to_pdf(process_files(folder), folder, cwd)
	logger.info("Files can be found here: {}\r".format(cwd))
