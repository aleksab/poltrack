#!/bin/bash
echo "Creating word2vec vectors"
python scripts/generate_word2vec.py data/signalmedia-1m.jsonl data/signalmedia.word2vec.model


