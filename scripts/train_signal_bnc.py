import os.path
import sys, gensim, logging,codecs,gzip
from numpy import ones

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

def update(model, data, sentences):
    model.syn0_lockf = ones(len(model.vocab), dtype="float32")

    logging.info("Training with new data...")
    model.train(data,total_examples=sentences)

    return model

if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))

    # check and process input arguments
    if len(sys.argv) < 4:
        print globals()['__doc__'] % locals()
        sys.exit(1)
    model, inpath, outpath = sys.argv[1:5]

    base_model = gensim.models.Word2Vec.load(model)
    base_model.batch_words = 10000
    previous_model = None

    #groups = "1 2-3 4-5-6 7-8 9-10 11-12-13 14-15 16-17 18-19-20 21-22 23-24 25-26-27 28-29 30".split()
    groups = "23-24 25-26-27 28-29 30".split()

    for group in groups:
        logger.info("Processing group %s" % group)

        filename = "signalmedia-1m.split.y2015.m9.d%s.processed" % (group)
        data = gensim.models.word2vec.LineSentence(inpath + filename)
        sentences = len(open(inpath + filename,'r').readlines())

        if previous_model == None:
            previous_model = base_model

        output = "bnc_model.d%s" % (group)

        updated_model = update(previous_model, data, sentences)
        updated_model.save(outpath + output)
        previous_model = updated_model

    logger.info("Done")