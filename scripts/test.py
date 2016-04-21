#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import os.path
import sys
import multiprocessing
import json
import re
import hunspell
from pip.util import cache_download

import nltk

from nltk import word_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem import SnowballStemmer
from nltk.corpus import wordnet

hobj = hunspell.HunSpell('/usr/share/hunspell/en_US.dic', '/usr/share/hunspell/en_US.aff')
cachedStopWords = stopwords.words("english")
lemmatizer = WordNetLemmatizer()
snowball_stemmer = SnowballStemmer("english")
wordnet_lemmatizer = WordNetLemmatizer()

tokens = "In worchester Fred gave a salution to John"

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

for token in tokens.split():
    print "Stemming word %s" % token
    print PorterStemmer().stem(token)
    print LancasterStemmer().stem(token)
    print hobj.stem(token)
    print snowball_stemmer.stem(token)
    print "-------"

print "Lemmatizing with pos tagging"
tagged = nltk.pos_tag(tokens.split())
for word in tagged:
    print "Word %s (%s) => %s" % (word[0], wordnet_lemmatizer.lemmatize(word[0], get_wordnet_pos(word[1])), word[1])