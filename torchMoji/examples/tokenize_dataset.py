"""
Take a given list of sentences and turn it into a numpy array, where each
number corresponds to a word. Padding is used (number 0) to ensure fixed length
of sentences.
"""

from __future__ import print_function, unicode_literals
import json
from torchMoji.torchmoji.sentence_tokenizer import SentenceTokenizer

with open('../model/vocabulary.json', 'r') as f:
    vocabulary = json.load(f)

st = SentenceTokenizer(vocabulary, 30)
test_sentences = [
    '\u2014 -- \u203c !!\U0001F602',
    'Hello world!',
    'This is a sample tweet #example',
    ]

tokens, infos, stats = st.tokenize_sentences(test_sentences)

print(tokens)
print(infos)
print(stats)
