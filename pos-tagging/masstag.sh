#!/bin/bash
COUNTER=1

while IFS=$'\t' read -r -a myArray
do
#echo $COUNTER
echo "NEWDOCUMENTBEGINSHERE!"
echo -e "${myArray[0]}\t${myArray[1]}\t${myArray[2]}"
echo "${myArray[4]}" | java -cp stanford-postagger.jar edu.stanford.nlp.tagger.maxent.MaxentTaggerServer -client -port $1
echo "${myArray[5]}" | java -cp stanford-postagger.jar edu.stanford.nlp.tagger.maxent.MaxentTaggerServer -client -port $1
COUNTER=`expr $COUNTER + 1`
done < /dev/stdin

