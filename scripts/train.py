#!/usr/bin/python2
# coding: utf-8

import sys, gensim, logging,codecs,gzip
from numpy import ones

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

def update(model, data, sentences):
    model.syn0_lockf = ones(len(model.vocab), dtype="float32")

    logging.info("Training with new data...")
    model.train(data,total_examples=sentences)

    return model

base_model = gensim.models.Word2Vec.load(sys.argv[1])


days = "september 14-15 16-17 18-19-20 21-22 23-24 25-26-27 28-29-30".split()

previous_model = None

for day in days:
    print >> sys.stderr, day
    fname = day+'.txt.gz'
    sentences = len(gzip.open(fname,'r').readlines())
    data = gensim.models.word2vec.LineSentence(fname)

    if previous_model == None:
	previous_model = base_model

    updated_model = update(previous_model, data, sentences)
    updated_model.save(day+'.model')
    previous_model = updated_model
