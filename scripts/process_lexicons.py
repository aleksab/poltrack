import os.path
import sys, gensim, logging,codecs,gzip

afinn = dict(map(lambda (k,v): (k,int(v)), [ line.split('\t') for line in open(sys.argv[1]) ]))
print afinn["Good".lower()]

print len([key for key, score in afinn.items() if score == 5])
print [key for key, score in afinn.items() if score == 4]