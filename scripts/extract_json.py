#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import os.path
import sys
import multiprocessing
import json
import re

from nltk import word_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords

cachedStopWords = stopwords.words("english")
 
def tokenize(text):
    min_length = 3
    words = map(lambda word: word.lower(), word_tokenize(text))
    words = [word for word in words
                  if word not in cachedStopWords]
    tokens =(list(map(lambda token: PorterStemmer().stem(token),words)))
    p = re.compile('[a-zA-Z]+')
    filtered_tokens = list(filter(lambda token:
        p.match(token) and len(token)>=min_length, tokens))
    return filtered_tokens
 
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
    inp, outp = sys.argv[1:3]
 
    output = open(outp, 'w');
    with open(inp) as f:
	for line in f:
	    obj = json.loads(line)
	    str = tokenize(obj["content"]) # remove if you dont' want tokenized documents
	    if str:
	        output.write(" ".join(str).encode("utf8"))
		output.write("\n")

    output.close()
