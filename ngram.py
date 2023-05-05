import nltk
from nltk.util import ngrams
from collections import Counter

# read in the two files
with open('pred4 (1).txt', 'r') as f:
    file1 = f.read()
with open('target_test_bpe.txt', 'r') as f:
    file2 = f.read()

# define the number of n-grams
n = 3

# tokenize the text in each file
tokens1 = nltk.word_tokenize(file1)
tokens2 = nltk.word_tokenize(file2)

# generate n-grams for each file
ngrams1 = ngrams(tokens1, n)
ngrams2 = ngrams(tokens2, n)

# count the frequency of each n-gram in each file
ngram_freq1 = Counter(ngrams1)
ngram_freq2 = Counter(ngrams2)

# compute the n-gram overlap
overlap = 0
for ngram, freq in ngram_freq1.items():
    overlap += min(freq, ngram_freq2[ngram])

# compute the precision, recall, and F1 score
precision = overlap / len(ngram_freq1)
recall = overlap / len(ngram_freq2)
f1_score = 2 * (precision * recall) / (precision + recall)

print("Precision:", precision)
print("Recall:", recall)
print("F1 score:", f1_score)
