#!/usr/bin/python2
# coding: utf-8

import json
import sys, gensim, logging,codecs,gzip
from numpy import exp, log, dot, zeros, outer, random, dtype, float32 as REAL,\
uint32, seterr, shape, array, uint8, vstack, fromstring, sqrt, newaxis,\
ndarray, empty, sum as np_sum, prod, ones, ascontiguousarray

from six import itervalues

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

def load_signal(input):
    sentences = []
    with open(input) as f:
            for line in f:
                obj = json.loads(line)
                sentences.append(obj["title"] + " " + obj["content"])

    return sentences

sentences = load_signal(sys.argv[1])

output = open(sys.argv[2], 'w')
for sentence in sentences:
    output.write("%s\n" % (sentence.encode('utf8')))
output.close()