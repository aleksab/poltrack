#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import os.path
import sys
import json
import re
import nltk

from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet

cachedStopWords = stopwords.words("english")
lemmatizer = WordNetLemmatizer()

def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN


def removeStopWords(input):
    min_length = 3

    words = [word.lower() for word in input
                  if word.lower() not in cachedStopWords]

    p = re.compile('[a-zA-Z]+')
    filtered_tokens = list(filter(lambda token:
        p.match(token) and len(token)>=min_length, words))
    return filtered_tokens


def lemmatize(input):

    words = []

    sentences = nltk.sent_tokenize(input)
    for sentence in sentences:
        tokenized = nltk.word_tokenize(sentence)
        tokenized = removeStopWords(tokenized)
        tagged = nltk.pos_tag(tokenized)

        for word in tagged:
            words.append(lemmatizer.lemmatize(word[0], get_wordnet_pos(word[1])))

    # convert back to string
    return " ".join(words)


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
    inp, outp = sys.argv[1:3]

    output = open(outp, 'w');
    with open(inp) as f:
        for line in f:
            obj = json.loads(line)
            obj["content"] = lemmatize(obj["content"])
            obj["title"] = lemmatize(obj["title"])
            output.write(json.dumps(obj, ensure_ascii=False).encode("utf8"))

    output.close()

    print "Done"