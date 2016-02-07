import sys
import random
from csv import DictReader, DictWriter

def csvtotext (file, out):
	data = list(DictReader(open(file, 'r')))
	output = open(out, 'w')
	txt= []
	print "converting csv to txt"
	sys.stdout = output
	for x in data:
		if "RT" and "@" not in x['text']:
			print x['text']
	sys.stdout = sys.__stdout__