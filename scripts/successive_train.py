#!/usr/bin/python2
# coding: utf-8

import sys, gensim, logging,codecs,gzip
from numpy import exp, log, dot, zeros, outer, random, dtype, float32 as REAL,\
uint32, seterr, shape, array, uint8, vstack, fromstring, sqrt, newaxis,\
ndarray, empty, sum as np_sum, prod, ones, ascontiguousarray

from six import itervalues

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

def update(model, data, sentences, mincount=3):
    """
    Add new words from new data to the existing model's vocabulary,
    generate for them random vectors in syn0 matrix.
    For existing words, increase their counts by their frequency in the new data.
    Generate new negative sampling matrix (syn1neg).
    Then, train the existing model with the new data.
    """
    added_count = 0

    logging.info("Extracting vocabulary from new data...")
    newmodel = gensim.models.Word2Vec(min_count=mincount,sample=0,hs=0)
    newmodel.build_vocab(data)

    logging.info("Merging vocabulary from new data...")
    vocablen = len(model.index2word)
    sampleint = model.vocab[model.index2word[0]].sample_int
    words = 0
    newvectors = []
    newwords = []
    for word in newmodel.vocab:
	words += 1
	if word not in model.vocab:
	    v = gensim.models.word2vec.Vocab()
	    v.index = len(model.vocab)
	    model.vocab[word] = v
	    model.vocab[word].count = newmodel.vocab[word].count
	    model.vocab[word].sample_int = sampleint
	    model.index2word.append(word)
	    
	    random_vector = model.seeded_vector(model.index2word[v.index] + str(model.seed))
            newvectors.append(random_vector)
            
            added_count += 1
            newwords.append(word)
	else:
	    model.vocab[word].count += newmodel.vocab[word].count
	if words % 1000 == 0:
	    logging.info("Words processed: %s" % words)

    logging.info("added %d words into model from new data" % (added_count))

    logging.info("Adding new vectors...")
    alist = [row for row in model.syn0]
    for el in newvectors:
	alist.append(el)
    model.syn0 = array(alist)

    logging.info("Generating negative sampling matrix...")
    model.syn1neg = zeros((len(model.vocab), model.layer1_size), dtype=REAL)
    model.make_cum_table()

    model.neg_labels = zeros(model.negative + 1)
    model.neg_labels[0] = 1.

    model.syn0_lockf = ones(len(model.vocab), dtype=REAL)

    logging.info("Training with new data...")
    model.train(data,total_examples=sentences)

    return model,newwords

existing_model = sys.argv[1]
new_corpus = sys.argv[2]

sentences = len(gzip.open(new_corpus,'r').readlines())

model = gensim.models.Word2Vec.load(existing_model)
data = gensim.models.word2vec.LineSentence(new_corpus)

(updated_model, new_words) = update(model,data,sentences)

updated_model.save(existing_model.split('.')[0]+'_updated'+'.model')

