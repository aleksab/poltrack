#!/usr/bin/python2
# coding: utf-8
from __future__ import division
import codecs,sys,re,os

# Processing XML output of Stanford POS tagger, transforming it into sequences of lemmas with POS tags.

stopwords = set([w.strip() for w in open('stopwords_en.txt','r').readlines()])

for line in sys.stdin:
    data = line.strip()
    if data == "NEWDOCUMENTBEGINSHERE!":
	print '\n'
	continue
    elif data.startswith('2015'):
	print data+'\t',
	continue
    elif data.startswith('<'):
	if '</sentence>' in data or '<sentence' in data:
	    continue
	if '<word' in data:
	    elements = data.split('"')
	    lemma = elements[5]
	    pos = elements[3]
	    if lemma.strip() in stopwords or lemma.strip().lower() == pos.strip().lower() or lemma.strip().isdigit() or len(pos.strip()) < 2 or len(lemma.strip()) < 2 or pos.strip() == "CD" or "&amp" in lemma:
		continue
	    print lemma.strip().lower()+'_'+pos.strip()[:2],

