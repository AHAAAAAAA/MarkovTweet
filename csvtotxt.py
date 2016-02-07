import sys
import random
from csv import DictReader, DictWriter

def csvtotext (file, out):
	data = list(DictReader(open(file, 'r')))
	output = open(out, 'w')
	txt= []
	sys.stdout = 'tweets.txt'
	for x in data:
		if "RT" and "@" not in x['text']:
			print x['text']
