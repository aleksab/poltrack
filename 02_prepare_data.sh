#!/bin/bash
echo "Preparing singal media corpus"
python scripts/extract_json.py data/signalmedia-1m.jsonl data/signalmedia.data
