#!/usr/bin/python2
# coding: utf-8
import sys

for line in sys.stdin:
    res = line.strip().split()
    lemmas = []
    for w in res:
	(word,pos) = w.split('_')
	lemmas.append(word.strip())
    print ' '.join(lemmas)