# Evaluation_Metrics
This repository contains various methods to evaluate the model performance.

# sacreBLEU
## Installation
Install the official Python module from PyPI (Python>=3.6 only):
```
pip install sacrebleu
```

## Using your own reference file
SacreBLEU knows about common test sets (as detailed in the --list example above), but you can also use it to score system outputs with arbitrary references. In this case, we need to provide detokenized reference and hypotheses files:
```
# Let's save the reference to a text file
$ sacrebleu -t wmt17 -l en-de --echo ref > ref.detok.txt

# Option 1: Pass the reference file as a positional argument to sacreBLEU
$ sacrebleu ref.detok.txt -i output.detok.txt -m bleu -b -w 4
20.7965

# Option 2: Redirect the system into STDIN (Compatible with multi-bleu.perl way of doing things)
$ cat output.detok.txt | sacrebleu ref.detok.txt -m bleu -b -w 4
20.7965
```
# Meteor
 METEOR (Metric for Evaluation of Translation with Explicit ORdering) is a machine translation evaluation metric, which is calculated based on the harmonic mean of precision and recall, with recall weighted more than precision.

METEOR is based on a generalized concept of unigram matching between the machine-produced translation and human-produced reference translations. Unigrams can be matched based on their surface forms, stemmed forms, and meanings. Once all generalized unigram matches between the two strings have been found, METEOR computes a score for this matching using a combination of unigram-precision, unigram-recall, and a measure of fragmentation that is designed to directly capture how well-ordered the matched words in the machine translation are in relation to the reference.
# N-Gram
n-grams are Markov models that estimate words from a fixed window of previous words. n-gram probabilities can be estimated by counting in a corpus
and normalizing (the maximum likelihood estimate). n-gram language models are evaluated extrinsically in some task, or intrinsically using perplexity. We can use these models as an evaluation metrices for our language model.

