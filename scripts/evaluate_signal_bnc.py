import os.path
import sys, gensim, logging,codecs,gzip

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

afinn = dict(map(lambda (k,v): (k,int(v)), [ line.split('\t') for line in open(sys.argv[1]) ]))

positive = [key for key, score in afinn.items() if score > 0]
negative = [key for key, score in afinn.items() if score < 0]

print 'positive words:', len(positive)
print 'negative words:', len(negative)

words = set()
words.add("turnbull")

models = {}
for m in sys.argv[2:]:
	models[m] = gensim.models.Word2Vec.load(m)
	models[m].init_sims(replace=True)

for m in models:
    print 'Checking model', m
    model = models[m]

    for word in words:
        print 'Checking word', word

        total_positive = 0
        biggest_positive = 0
        pword = ''
        for pos in positive:
            if pos in model.vocab:
                sim = model.similarity(word, pos)
                if sim > 0:
                    total_positive += model.similarity(word, pos)

                    if sim > biggest_positive:
                        biggest_positive = sim
                        pword = pos
                #else:
                    #print 'This positive word is NOT related', pos, sim
        print 'Positive words:', total_positive
        print 'Most positive word:', pword, '=>', biggest_positive

        total_negative = 0
        biggest_negative = 0
        nword = ''
        for neg in negative:
            if neg in model.vocab:
                sim = model.similarity(word, neg)
                if sim > 0:
                    total_negative += model.similarity(word, neg)

                    if sim > biggest_negative:
                        biggest_negative = sim
                        nword = pos
                #else:
                #    print 'This negative word is NOT related', neg, sim
        print 'Negative words:', total_negative
        print 'Most negative word:', nword, '=>', biggest_negative

    print '------'