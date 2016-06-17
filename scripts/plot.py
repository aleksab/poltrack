#!/usr/bin/python2
# coding: utf-8

"""
Plotting expression of evaluative features. Takes as an input a json file with distances and a named entity.
"""

import matplotlib.pyplot as plt
import json, codecs, sys
import numpy as np

data = json.loads(codecs.open(sys.argv[1],'r','utf-8').read())

name = sys.argv[2].decode('utf-8')

entity = data[name]


height = 1
adjectives = []
expression = []
polarity = []
for i in entity['positive']:
    adjectives.append(i.split('_')[0])
    value = entity['positive'][i]
    expression.append(abs(value))
    if value < 0:
	polarity.append(1)
    else:
	polarity.append(0)

for i in entity['negative']:
    adjectives.append(i.split('_')[0])
    value = entity['negative'][i]
    expression.append(abs(value))
    if value > 0:
	polarity.append(1)
    else:
	polarity.append(0)

y_pos = np.arange(len(adjectives))
barlist = plt.barh(y_pos, expression, align='center', alpha=0.4, height=height)

for bar in xrange(len(polarity)):
    if polarity[bar] == 1:
	barlist[bar].set_color('r')


plt.yticks(y_pos, adjectives)


plt.xlabel('Expression')
plt.title(name)

plt.show()