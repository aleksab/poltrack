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

#name = sys.argv[2].decode('utf-8')

for name in data:
    entity = data[name]
    sentiment = {'positive':[], 'negative':[]}

    example = entity["positive"].keys()[0]
    periods = len(entity["positive"][example])

    for period in range(periods):
	distances = []
	for i in entity['positive']:
	    value = entity['positive'][i][period]
	    distances.append(value)
	sentiment['positive'].append(np.average(distances))

	distances = []
	for i in entity['negative']:
	    value = entity['negative'][i][period]
	    distances.append(value)
	sentiment['negative'].append(np.average(distances))

    dates = range(periods)
    plt.plot(dates, sentiment['positive'], label='Positive sentiment', color='g')
    plt.plot(dates, sentiment['negative'], label='Negative sentiment', color='r')

    plt.ylabel('Expression')
    plt.xlabel('Dates')
    plt.title(name)
    plt.legend()
    #plt.show()
    plt.savefig(name+'.png')
    plt.close()