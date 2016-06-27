#!/usr/bin/python2
# coding: utf-8

import sys, gensim, logging
from itertools import combinations

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

#afinn = dict(map(lambda (k,v): (k,int(v)), [ line.split('\t') for line in open(sys.argv[1]) ]))
#positive = [key for key, score in afinn.items() if score > 0]
#negative = [key for key, score in afinn.items() if score < 0]

def jaccard(set_1, set_2):
    n = len(set_1.intersection(set_2))
    return n / float(len(set_1) + len(set_2) - n)

def jaccard_f(words,models,row=10):
    distances = {}
    for word in words:
        distances[word] = {}
        associations = {}
        for m in models:
            model = models[m]
            word_neighbors = [i[0] for i in model.most_similar(positive=[word], topn=row)]
            associations[m.replace('.model', '')] = set(word_neighbors)
        for pair in combinations(associations.keys(), 2):
            similarity = jaccard(associations[pair[0]], associations[pair[1]])
            if len(associations.keys()) > 2:
                distances[word]['-'.join(pair)] = similarity
            else:
                distances[word] = similarity
            print 'Similarity of', word, 'between', pair[0], 'and', pair[1], ":", similarity
            print 'associates in', pair[0], ' '.join(associations[pair[0]]), '\n', 'associates in', pair[1], ' '.join(associations[pair[1]])
            print '~~~~~~'

            #print sum(map(lambda word: afinn.get(word, 0), associations[pair[0]]))
            #print sum(map(lambda word: afinn.get(word, 0), associations[pair[1]]))
        print '======================='
    return distances

if __name__ == '__main__':
    words = set()

    words.add("turnbull")
    #for line in open(sys.argv[1], 'r'):
	#word = line.strip().decode('utf-8')
	#if not word.startswith('#'):
	#    words.add(word.strip())

    row = 25 # How many nearest neighbors to take into account from vector model
    models = {}
    for m in sys.argv[2:]:
	    models[m] = gensim.models.Word2Vec.load(m)
	    models[m].init_sims(replace=True)
	
    print >> sys.stderr, 'Total words to process:', len(words)
    print >> sys.stderr, "Total models:", len(models)

    neighbors = {}
    jaccard_f(words, models, row)
