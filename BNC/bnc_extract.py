#!/usr/bin/python2
# coding: utf-8
import sys,os
from xml.dom import minidom

argument = sys.argv[1]

files = os.listdir(argument)
files = [f for f in files if f.endswith('.xml')]

for f in files:
    doc = minidom.parse(argument+f)
    node = doc.documentElement

    sentences = doc.getElementsByTagName("s")
    for sentence in sentences:
	words = sentence.getElementsByTagName("w")
	for word in words:
	    lemma = word.getAttributeNode('hw').nodeValue.strip()
	    pos = word.getAttributeNode('c5').nodeValue.strip()
	    print lemma.encode('utf-8')+'_'+pos.encode('utf-8'),
	print '\n'
