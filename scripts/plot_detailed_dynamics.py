#!/usr/bin/python2
# coding: utf-8

"""
Plotting expression of evaluative features. Takes as an input a json file with distances and a named entity.
"""

import matplotlib.pyplot as plt
import json, codecs, sys, gzip
import numpy as np

datafile = gzip.open(sys.argv[1],'r')
contents = datafile.read()
datafile.close()

contents = contents.decode('utf-8')


data = json.loads(contents)

name = sys.argv[2].decode('utf-8')

entity = data[name]

adjectives = []
expression = {}
polarity = {}
for i in entity['positive']:
    values = entity['positive'][i]
    adjective = i.split('_')[0]
    adjectives.append(adjective)
    expression[adjective] = []
    polarity[adjective] = []
    for value in values:
	expression[adjective].append(abs(value))
	if value < 0:
	    polarity[adjective].append(1)
	else:
	    polarity[adjective].append(0)
	
for i in entity['negative']:
    values = entity['negative'][i]
    adjective = i.split('_')[0]
    adjectives.append(adjective)
    expression[adjective] = []
    polarity[adjective] = []
    for value in values:
	expression[adjective].append(abs(value))
	if value > 0:
	    polarity[adjective].append(1)
	else:
	    polarity[adjective].append(0)

for adj in adjectives:
    dates = range(len(expression[adj]))
    plt.plot(dates, expression[adj], label=adj)

#for bar in xrange(len(polarity)):
#    if polarity[bar] == 1:
#	barlist[bar].set_color('r')

plt.ylabel('Expression')
plt.xlabel('Dates')
plt.title(name)
plt.legend()

plt.show()