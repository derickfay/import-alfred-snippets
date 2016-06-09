#!/usr/bin/python

# importSnippets.py
#
# generates Alfred 3 json snippets from a csv file
#
# written for python 2.7.10


import csv
import json
import os, binascii

sourceFile = 'snippets.csv'
fieldNames = ['name','keyword','content']

with open (sourceFile, 'rt') as csvfile:
	reader = csv.DictReader(csvfile, fieldnames=fieldNames)
	for row in reader:
		uid = binascii.b2a_hex(os.urandom(15))
		output = json.dumps({"alfredsnippet" : {"snippet" : row['content'], "uid": uid, "name" : row['name'], "keyword" : row['keyword']}}, sort_keys=False, indent=4, separators=(',', ': '))
		outputFile = row['name']+" ["+uid+"].json"
		f = open(outputFile, 'w')
		f.write(output)
		f.close()
