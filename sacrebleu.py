import nltk
from nltk.translate.bleu_score import sentence_bleu
from nltk.tokenize import word_tokenize

# read in the two files
with open('pred4 (1).txt', 'r') as f:
    file1 = f.read()
with open('target_test_bpe.txt', 'r') as f:
    file2 = f.read()

# tokenize the text in each file
tokens1 = word_tokenize(file1)
tokens2 = word_tokenize(file2)

# calculate the BLEU score
bleu_score = sentence_bleu([tokens1], tokens2) * 100

print("BLEU score (out of 100):", bleu_score)
