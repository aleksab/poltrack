#!/usr/bin/python2
# coding: utf-8
from __future__ import division
import codecs,sys,re,json

stopwords = set([w.strip() for w in open('stopwords_en.txt','r').readlines()])

for line in sys.stdin:
    res = json.loads(line.strip().decode('utf-8'))
    id = res['id'].replace('\r\n',' ').replace('\n','.').replace('\r','.').replace('\t',' ').encode('utf-8','replace').strip()
    published = res['published'].replace('\r\n','.').replace('\n','.').replace('\r','.').replace('\t',' ').encode('utf-8','replace').strip()
    source = res["source"].replace('\r\n','.').replace('\n','.').replace('\r','.').replace('\t',' ').encode('utf-8','replace').strip()
    mediatype = res["media-type"].replace('\r\n','.').replace('\n','.').replace('\r','.').replace('\t',' ').encode('utf-8','replace').strip()
    content = res["content"].replace('\r\n','.').replace('\n','.').replace('\r','.').replace('\t',' ').encode('utf-8','replace').strip()
    title = res["title"].replace('\r\n','.').replace('\n','.').replace('\r','.').replace('\t',' ').encode('utf-8','replace').strip()
    print id+'\t'+published+'\t'+source+'\t'+mediatype+'\t'+title+'\t'+content