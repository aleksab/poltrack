#!/usr/bin/python2
# coding: utf-8
import sys

import gensim, logging,json
from sentence.ranking import Ranking
from evaluation.ranking.segment import kendall_tau

def generate_ranks(w1, w2):
    all_words = set(w1 + w2)
    rank1 = []
    rank2 = []
    for word in all_words:
        if word in w1:
            rank1.append(w1.index(word) + 1)
        else:
            rank1.append(len(w1) + 1)
        if word in w2:
            rank2.append(w2.index(word) + 1)
        else:
            rank2.append(len(w2) + 1)
    return rank1, rank2

def kendall(words,models,row, list_of_models):
    distances = {}
    for m in range(0, len(list_of_models) -1):
	distances[list_of_models[m] + ' ' + list_of_models[m + 1]] = {}
    for word in words:
        associations = {}
        list_of_models = []
        for m in models:
            model = models[m]
            if word not in model:
        	continue
            word_neighbors = [i[0] for i in model.most_similar(positive=[word], topn=row)]
            associations[m.replace('.model', '')] = word_neighbors
            list_of_models.append(m.replace('.model', ''))
        for m in range(0, len(list_of_models) - 1):
            rank1_arr, rank2_arr = generate_ranks(associations[list_of_models[m]], associations[list_of_models[m + 1]])
            rank1 = Ranking(rank1_arr)
            rank2 = Ranking(rank2_arr)
            tau = (kendall_tau(rank1, rank2).tau + 1)/2
            distances[list_of_models[m] + ' ' + list_of_models[m + 1]][word] = {}
            distances[list_of_models[m] + ' ' + list_of_models[m + 1]][word]['coeff'] = tau
            distances[list_of_models[m] + ' ' + list_of_models[m + 1]][word]['neighbors'] = {}
            distances[list_of_models[m] + ' ' + list_of_models[m + 1]][word]['neighbors'][list_of_models[m]] = associations[list_of_models[m]]
            distances[list_of_models[m] + ' ' + list_of_models[m + 1]][word]['neighbors'][list_of_models[m + 1]] = associations[list_of_models[m + 1]]
    return distances

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    words = set()
    if sys.argv[1] != 'ALL':
	for line in open(sys.argv[1], 'r'):
	    word = line.strip().decode('utf-8')
            if not word.startswith('#'):
        	words.add(word.strip())
    for m in sys.argv[2:]:
	models[m] = gensim.models.Word2Vec.load(m)
	models[m].init_sims(replace=True)
	if sys.argv[1] == 'ALL':
	    if len(words) == 0:
        	words = set(models[m].vocab.keys())
            else:
        	words = words & set(models[m].vocab.keys())

    print >> sys.stderr, 'Total words to process:', len(words)
    print >> sys.stderr, "Total models:", len(models)
    kendall(words,models,row=10)
