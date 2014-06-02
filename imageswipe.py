#!/usr/bin/python

import sys, getopt, PIL, Image

usage = """
Usage: imageswipe.py [ARGUMENT] <path to first image> <path to second image>

Required Argument:
-r, --resize	Specify an image width.
-o, --original	Keep original image size.

Optional Argument:
-h, --help	Display usage information. 

NOTE: Images must be the same size.
"""

def main():
"""
Copyright (c) 2014 Michigan Tech Research Institute
3600 Green Court, Suite 100, Ann Arbor, MI, 48104

This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License (http://creativecommons.org/licenses/by-nc-sa/3.0/).
"""
	try:
		opts, args = getopt.getopt(sys.argv[1:],"r:ho",["resize", "help", 'original'])
	except getopt.GetoptError:
		print usage
		sys.exit(2)
	for opt, arg in opts:
		if opt in ('-h', '--help'):
			print usage
			sys.exit()

		elif opt in ("-r", '--resize'):
			width = int(sys.argv[2])
			im = Image.open(sys.argv[3])
			ratio = (width/float(im.size[0]))
			height = int(float(im.size[1]*ratio))
			im = im.resize((width,height), Image.ANTIALIAS)
			im.save('images/left.jpg')
		
			im = Image.open(sys.argv[4])
			ratio = (width/float(im.size[0]))
			height = int(float(im.size[1]*ratio))
			im = im.resize((width,height), Image.ANTIALIAS)
			im.save('images/right.jpg')

			dim = open('./width.txt','r+')
			dim.write(str(im.size[0]))
			dim = open('./height.txt','r+')
			dim.write(str(im.size[1]))
			sys.exit()

		elif opt in ('-o','--original'):
			im = Image.open(sys.argv[2])
			im.save('images/left.jpg')
			im = Image.open(sys.argv[3])
			im.save('images/right.jpg')

			dim = open('./width.txt','r+')
			dim.write(str(im.size[0]))
			dim = open('./height.txt','r+')
			dim.write(str(im.size[1]))
			sys.exit()
    
if __name__ == "__main__":
	main()

