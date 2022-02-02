import json
import string
import numpy as np
from nltk.util import ngrams
from collections import Counter, defaultdict

# LAMBDA = 0.0000000001

# class variabledefaultdict(defaultdict):
#     def __missing__(self, key):
#         return self.default_factory(key)


# def laplace(observed, total, total_tags):
#     return (observed + LAMBDA) / (total + LAMBDA * total_tags)

# def default_emission_laplace(key, total_tags):
#     word, tag = key
#     return laplace(0, tag_count[tag], total_tags)

# def default_transition_laplace(key, total_tags):
#     first, second, third = key
#     return laplace(0, bigram_count[(first, second)], total_tags)

def remove_punctuations(data):
    result = [line.translate(str.maketrans('', '', string.punctuation)) for line in data]
    return result

def load_dataset():
    data_file = open('penn-data.json')
    dataset = np.array(json.load(data_file), dtype=object)
    return remove_punctuations(dataset[:, 0]), dataset[:, 1]

def generate_emission_matrix(x, y):
    word_tag_count = defaultdict(lambda: 0)
    tag_count = defaultdict(lambda: 0)

    for line, tags in zip(x, y):
        for word, tag in zip(line.split(), tags):
            tag_count[tag] += 1
            word_tag_count[(word, tag)] += 1
    
    emission_matrix = defaultdict(lambda: 0.0000000001)
    
    for word_tag in word_tag_count.keys():
        word, tag = word_tag
        emission_matrix[word_tag] = word_tag_count[word_tag] / tag_count[tag]

    return emission_matrix

def generate_transition_matrix(y):
    trigram_tags = []
    for tag_list in y:
        tag_list = ["*", "*"] + tag_list + ["STOP"]
        trigram_tags.extend(ngrams(tag_list, 3))
    trigram_count = dict(Counter(trigram_tags))

    bigram_tags = []
    for tag_list in y:
        tag_list = ["*", "*"] + tag_list + ["STOP"]
        bigram_tags.extend(ngrams(tag_list, 2))
    bigram_count = dict(Counter(bigram_tags))

    transition_matrix = defaultdict(lambda: 0.0000000001)

    for trigram in trigram_count:
        first, second, third = trigram
        transition_matrix[trigram] = trigram_count[trigram] / bigram_count[(first, second)]

    return transition_matrix