import nltk
from nltk.translate.meteor_score import meteor_score
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer

# read in the two files
with open('pred4 (1).txt', 'r') as f:
    file1 = f.read()
with open('target_test_bpe.txt', 'r') as f:
    file2 = f.read()

# tokenize and lemmatize the text in each file
lemmatizer = WordNetLemmatizer()
sentences1 = sent_tokenize(file1)[:5]
sentences2 = sent_tokenize(file2)[:5]
tokens1 = [lemmatizer.lemmatize(token.lower()) for sentence in sentences1 for token in word_tokenize(sentence)]
tokens2 = [lemmatizer.lemmatize(token.lower()) for sentence in sentences2 for token in word_tokenize(sentence)]

# calculate the METEOR score
meteor_score = meteor_score([tokens1], tokens2)

print("METEOR score:", meteor_score)
