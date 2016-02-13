#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import os.path
import sys
import multiprocessing
import json
 
 
 
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
 
    data = []
    with open(inp) as f:
	for line in f:
	   if line.strip():
	       data.append(json.loads(line))
    logger.info("loaded %s lines", len(data))

    with open(outp, 'w') as f:
	for obj in data:
    	    f.write(obj["content"].replace("\n","").encode('utf8'))
	    f.write('\n')
    
