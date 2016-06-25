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
    res = line.strip().split('\t')
    (freq, entity) = res
    persons[entity] = {}

print >> sys.stderr, "Interesting persons:", len(persons)

input_path = sys.argv[2]

groups = "1 2-3 4-5-6 7-8 9-10 11-12-13 14-15 16-17 18-19-20 21-22 23-24 25-26-27 28-29 30".split()

for group in groups:

    name = "bnc_model.d%s" % (group)
    filename = input_path + name
    print 'Checking model', filename

    model = gensim.models.Word2Vec.load(filename)
    model.init_sims(replace=True)
    print >> sys.stderr, model
    for dataset in ("positive","negative","ambiguous"):
        for person in persons:
            if not dataset in persons[person]:
                persons[person][dataset] = {}

            if person in model.vocab:
                for el in eval(dataset):
                    if not el in persons[person][dataset]:
                        persons[person][dataset][el] = []

                    if el in model.vocab:
                        distance = model.similarity(person,el)
                        persons[person][dataset][el].append(distance)

    print "Done"


with open('persons.evaluation', 'w') as f:
    f.write(json.dumps(persons,ensure_ascii=False).encode('utf-8'))
