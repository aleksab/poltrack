#!/usr/bin/python2
# coding: utf-8

import json
import sys, gensim, logging,codecs,gzip
from numpy import exp, log, dot, zeros, outer, random, dtype, float32 as REAL,\
uint32, seterr, shape, array, uint8, vstack, fromstring, sqrt, newaxis,\
ndarray, empty, sum as np_sum, prod, ones, ascontiguousarray

from six import itervalues

def update(model, data, sentences):
    model.syn0_lockf = ones(len(model.vocab), dtype="float32")

    logging.info("Training with new data...")
    model.train(data,total_examples=sentences)

    return model

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

with open(sys.argv[1]) as data_file:
    data = json.load(data_file)

print data['wenger']

for word in data:
    if data[word]['positive'] == {}:
        print 'Word is missing', word



#model = gensim.models.Word2Vec.load('/data/poltrack/data/signal_split/bnc_models/bnc_model.d1')
#print model.most_similar('obama')

#base_model = gensim.models.Word2Vec.load('/data/poltrack/data/bnc/bnc.model')
#print base_model.most_similar('putin')

#sentences = len(open('/data/poltrack/data/signal_split/processed/signalmedia-1m.split.y2015.m9.d1.processed','r').readlines())
#data = gensim.models.word2vec.LineSentence('/data/poltrack/data/signal_split/processed/signalmedia-1m.split.y2015.m9.d1.processed')
#updated_model = update(base_model, data, sentences)

#print updated_model.most_similar('obama')