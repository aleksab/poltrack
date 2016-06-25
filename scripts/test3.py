import json
import sys, gensim, logging,codecs,gzip
from numpy import ones

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

afinn = dict(map(lambda (k,v): (k,int(v)), [ line.split('\t') for line in open(sys.argv[1]) ]))

positive = [key for key, score in afinn.items() if score > 0]
negative = [key for key, score in afinn.items() if score < 0]
ambigous = [key for key, score in afinn.items() if score == 0]

print 'positive words:', len(positive)
print 'negative words:', len(negative)
print 'ambigous words:', len(ambigous)

with open('positive.lst', 'w') as f:
    for item in positive:
        f.write("%s\n" % item)

with open('negative.lst', 'w') as f:
    for item in negative:
        f.write("%s\n" % item)

with open('ambig.lst', 'w') as f:
    for item in ambigous:
        f.write("%s\n" % item)