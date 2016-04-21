#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import os.path
import sys
import json

from dateutil.parser import parse

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def get_file_name(prefix, input):
    date = parse(input)
    return "%s.split.y%i.m%i.d%i" % (prefix, date.year, date.month, date.day)


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

    name = os.path.splitext(os.path.basename(inp))[0]
    length = num_lines = sum(1 for line in open(inp))
    logger.info("Processing %s that has %i lines", inp, length)
    with open(inp) as f:
        counter = 0.0
        for line in f:
            obj = json.loads(line)

            file_name = outp + get_file_name(name, obj["published"])
            output = open(file_name, 'a')
            output.write(json.dumps(obj, ensure_ascii=False).encode("utf8"))
            output.write('\n')
            output.close()

            counter += 1.0

            if ((counter % 10) == 0):
                sys.stdout.write("Processed : %.2f   \r" % (100 * (counter / length)))
                sys.stdout.flush()

    logger.info("Done")