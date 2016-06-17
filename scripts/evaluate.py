#!/usr/bin/python2
# coding: utf-8

import sys, gensim, logging,codecs,os,codecs, json

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


entities = sys.argv[1]


negative = set()
positive = set()
ambiguous = set()

for line in codecs.open('negative.lst','r','utf-8'):
    res = line.strip()
    negative.add(res)
for line in codecs.open('positive.lst','r','utf-8'):
    res = line.strip()
    positive.add(res)
for line in codecs.open('ambig.lst','r','utf-8'):
    res = line.strip()
    ambiguous.add(res)
    
print >> sys.stderr, "Positive adjectives:", len(positive)
print >> sys.stderr, "Negative adjectives:", len(negative)
print >> sys.stderr, "Ambiguous adjectives:", len(ambiguous)

persons = {}


for line in codecs.open(entities,'r','utf-8'):
    res = line.strip().split()
    (freq, entity) = res
    persons[entity] = {}

print >> sys.stderr, "Interesting persons:", len(persons)

model_files = sys.argv[2:]

for m in model_files:
    model = gensim.models.Word2Vec.load(m)
    model.init_sims(replace=True)
    print >> sys.stderr, model
    for dataset in ("positive","negative","ambiguous"):
	for person in persons:
	    if not dataset in persons[person]:
		persons[person][dataset] = {}
	    for el in eval(dataset):
		distance = model.similarity(person,el)
		if not el in persons[person][dataset]:
		    persons[person][dataset][el] = []
		persons[person][dataset][el].append(distance)

print json.dumps(persons,ensure_ascii=False).encode('utf-8')