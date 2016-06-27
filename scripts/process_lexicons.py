import os.path
import sys, gensim, logging,codecs,gzip
from os.path import isfile, join
from os import listdir
import collections, re
from collections import defaultdict

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))

    # check and process input arguments
    if len(sys.argv) < 4:
        print globals()['__doc__'] % locals()
        sys.exit(1)
    afinnpath, inpath, outpath = sys.argv[1:5]

    afinn = dict(map(lambda (k,v): (k,int(v)), [ line.split('\t') for line in open(afinnpath) ]))

    positive = [key for key, score in afinn.items() if score > 0]
    negative = [key for key, score in afinn.items() if score < 0]
    ambiguous = [key for key, score in afinn.items() if score < 0]

    print 'positive words:', len(positive)
    print 'negative words:', len(negative)
    print 'ambiguous words:', len(ambiguous)

    bow = defaultdict(int)
    counter = 0
    files = [f for f in listdir(inpath) if isfile(join(inpath, f))]
    for file in files:
        sentences = open(inpath + file,'r').readlines()

        for sentence in sentences:
            for word in sentence.split(' '):
                bow[word.strip()] += 1
                counter += 1

    with open('positive.bow', 'w') as f:
        for word in positive:
            f.write("%d\t%s\n" % (bow[word], word))

    with open('negative.bow', 'w') as f:
        for word in negative:
            f.write("%d\t%s\n" % (bow[word], word))

    print 'Total words', counter