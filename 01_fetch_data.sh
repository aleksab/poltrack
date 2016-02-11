#!/bin/bash
#echo "Downloading 20 newsgroup"
#mkdir data
#wget http://qwone.com/~jason/20Newsgroups/20news-18828.tar.gz 
#tar zxf 20news.tar.gz
#mv 20news-18828 data/20news

echo "Downloading Signal Media corpus"
mkdir data
wget http://research.signalmedia.co/newsir16/signalmedia-1m.jsonl.gz
gunzip signalmedia-1m.jsonl.gz
mv signalmedia-1m.jsonl data/signalmedia-1m.jsonl

