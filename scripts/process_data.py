#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import os.path
import sys
import json
import re
import nltk

from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.tag.perceptron import PerceptronTagger
from os import listdir
from os.path import isfile, join

def process(input):
    sentences = []
    with open(input) as f:
            for line in f:
                obj = json.loads(line)
                sentences.append(obj["title"] + " " + obj["content"])

    return sentences

if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))

    # check and process input arguments
    if len(sys.argv) < 3:
        print globals()['__doc__'] % locals()
        sys.exit(1)
    inpath, outpath = sys.argv[1:3]

    groups = "1 2-3 4-5-6 7-8 9-10 11-12-13 14-15 16-17 18-19-20 21-22 23-24 25-26-27 28-29 30".split()

    for group in groups:
        logger.info("Processing group %s" % group)

        name = "signalmedia-1m.split.y2015.m9.d%s.processed" % (group)
        output = open(outpath + name, 'w')
        days = group.split("-")

        for day in days:
            filename = "signalmedia-1m.split.y2015.m9.d%s.prepared" % (day)
            with open(inpath + filename) as f:
                for line in f:
                    obj = json.loads(line)
                    output.write("%s\n" % (obj["content"].encode('utf8')))

        output.close()

    logger.info("Done")