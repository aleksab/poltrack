#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import os.path
import sys
import json
import operator
import nltk

from nltk.tag.perceptron import PerceptronTagger
from os import listdir
from os.path import isfile, join

tagger = PerceptronTagger()

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def extract_entity_names(t):
    entity_names = []

    if hasattr(t, 'label') and t.label:
        if t.label() == 'NE':
            entity_names.append(' '.join([child[0] for child in t]))
        else:
            for child in t:
                entity_names.extend(extract_entity_names(child))

    return entity_names

def extract_entities(input):

    entity_names = []

    sentences = nltk.sent_tokenize(input)
    for sentence in sentences:
        tokenized = nltk.word_tokenize(sentence)
        tagged = nltk.tag._pos_tag(tokenized, None, tagger)

        chunked = nltk.ne_chunk(tagged, binary=True)

        for tree in chunked:
            entity_names.extend(extract_entity_names(tree))

    return entity_names


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

    files = [f for f in listdir(inpath) if isfile(join(inpath, f))]
    for file in files:
        entities = {}
        length = num_lines = sum(1 for line in open(inpath + file))
        logger.info("Processing %s that has %i lines", inpath + file, length)
        with open(inpath + file) as f:
            counter = 0.0
            for line in f:
                obj = json.loads(line)
                local_entities = extract_entities(obj["content"])

                for local in local_entities:
                    if local in entities:
                        counter = entities[local]
                        entities[local] = counter + 1
                    else:
                        entities[local] = 1

                counter += 1.0

                if ((counter % 10) == 0):
                    sys.stdout.write("Processed : %.2f   \r" % (100 * (counter / length)))
                    sys.stdout.flush()

        sorted_entities = sorted(entities.items(), key=operator.itemgetter(1), reverse=True)

        name = outpath + file + ".entities"
        output = open(name, 'w')

        for entity in sorted_entities:
            output.write("%i\t%s\n" % (entity[1], entity[0].encode('utf8')))
        output.close()
        logger.info("Wrote entities for %s to %s", file, name)

    logger.info("Done")