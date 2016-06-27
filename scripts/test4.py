import json
import sys, gensim, logging,codecs,gzip
from numpy import ones
import operator

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

afinn = dict(map(lambda (k,v): (k,int(v)), [ line.split('\t') for line in open(sys.argv[1]) ]))

positive = [key for key, score in afinn.items() if score > 0]
negative = [key for key, score in afinn.items() if score < 0]
ambigous = [key for key, score in afinn.items() if score == 0]

positive_bow = dict(map(lambda (v,k): (k.lower(), int(v)), [ line.split('\t') for line in open('/data/poltrack/scripts/positive.bow') ]))
sorted_pbow = sorted(positive_bow.items(), key=operator.itemgetter(1), reverse=True)

negative_bow = dict(map(lambda (v,k): (k.lower(), int(v)), [ line.split('\t') for line in open('/data/poltrack/scripts/negative.bow') ]))
sorted_nbow = sorted(negative_bow.items(), key=operator.itemgetter(1), reverse=True)

print sorted_pbow
print sorted_nbow

with open('sorted_positive.lst', 'w') as f:
    for item in sorted_pbow:
        contrib = (item[1] / float(238822447)) * 100
        if contrib > 0.005:
            f.write("%d\t%s" % (item[1], item[0]))

with open('sorted_negative.lst', 'w') as f:
    for item in sorted_nbow:
        contrib = (item[1] / float(238822447)) * 100
        if contrib > 0.005:
            f.write("%d\t%s" % (item[1], item[0]))
