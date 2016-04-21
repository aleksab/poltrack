#!/bin/bash
echo "Splitting signal media corpus into months"
#mkdir data/signal_split/
#python scripts/split_data.py data/signalmedia-1m.jsonl data/signal_split/

echo "Preparing data"
#python scripts/prepare_data.py data/signal_split/signalmedia-1m.split.y2015.m7 data/signal_split/signalmedia-1m.split.y2015.m7.prepared

echo "Extracting entities"
python scripts/extract_entities.py data/signal_split/signalmedia-1m.split.y2015.m7 data/signal_split/signalmedia-1m.split.y2015.m7.entities
