import json
import sys, gensim, logging,codecs,gzip
from numpy import ones

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

base_model = gensim.models.Word2Vec.load(sys.argv[1])
model = gensim.models.Word2Vec.load(sys.argv[2])

logging.info("Similiarity before: %s" % base_model.similarity('company', 'china'));
logging.info("Similiarity after: %s" % model.similarity('company', 'china'));

logging.info("Similiarity after: %s" % base_model.most_similar('china'));
logging.info("Similiarity after: %s" % model.most_similar('china'));