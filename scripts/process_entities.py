#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import os.path
import sys
import logging
import os.path
import sys
import operator

def combine_dicts(a, b, op=operator.add):
    return dict(a.items() + b.items() +
        [(k, op(a[k], b[k])) for k in set(b) & set(a)])

if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))

    # check and process input arguments
    if len(sys.argv) < 3:
        print globals()['__doc__'] % locals()
        sys.exit(1)
    inpath, outpath = sys.argv[1:3]

    entities = dict()

    for day in range(1,31):
        logger.info("Processing day %s" % day)

        filename = "signalmedia-1m.split.y2015.m9.d%s.entities" % (day)
        fileentities = dict(map(lambda (v,k): (k, int(v)), [ line.split('\t') for line in open(inpath + filename) ]))

        logger.info("Found %d entities in %s", len(fileentities), filename)
        entities = combine_dicts(entities, fileentities)

    logger.info("Collected %d entities", len(entities))

    sorted_entities = sorted(entities.items(), key=operator.itemgetter(1), reverse=True)
    print sorted_entities[:25]

    logger.info("Done")