#!/bin/bash
#echo "Downloading 20 newsgroup"
#mkdir data
#wget http://qwone.com/~jason/20Newsgroups/20news-18828.tar.gz 
#tar zxf 20news.tar.gz
#mv 20news-18828 data/20news

#echo "Downloading Signal Media corpus"
#mkdir data
#wget http://research.signalmedia.co/newsir16/signalmedia-1m.jsonl.gz
#gunzip signalmedia-1m.jsonl.gz
#mv signalmedia-1m.jsonl data/signalmedia-1m.jsonl

echo "Downloading Norwegian Newspaper corpus"
#mkdir data/aviskorpus
#cd data/aviskorpus
#wget http://www.nb.no/sbfil/tekst/norsk_aviskorpus.zip
#unzip norsk_aviskorpus.zip
#cd 2/
#cat *.tar.gz | tar -zxf - -i

echo "Downloading BNC corpus"
#mkdir data/bnc
#cd data/bnc
#wget http://ltr.uio.no/~andreku/static/bnc.tar.gz
#tar zxf bnc.tar.gz

echo "Downloading AFinn lexicon"
cd data
wget http://www2.imm.dtu.dk/pubdb/views/edoc_download.php/6010/zip/imm6010.zip
unzip imm6010.zip
mv AFINN afinn
