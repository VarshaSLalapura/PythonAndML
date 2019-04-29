# 2-T-49-create_sentiment_featureset.py
# part 49/72, 6th part of DL, TF

from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import numpy as np
import random
import pickle
from collections import Counter
import os

lemmatizer = WordNetLemmatizer()
hm_lines = 10000000
path = '/home/varsha/Desktop/Datasets-Sentdex/TF'
pos_file = os.path.join(path, 'pos.txt')
neg_file = os.path.join(path, 'neg.txt')


def create_lexicon(pos, neg):
    lexicon = []
    for fi in [pos, neg]:
        with open(fi, 'r') as f:
            contents = f.readlines()
            # print('fn:', f)
            # print('contents', contents)  # prints all the lines of the file in a stretch
            for l in contents[:hm_lines]:  # up-to two lines
                all_words = word_tokenize(l.lower())  # separates the words in a line by comma and puts to a list
                # print('all_words', all_words)
                # print(type(all_words))
                lexicon += list(all_words)  # takes all the words in the list and puts to dict called lexicon
            # print(type(lexicon))
    # print(lexicon)  # this has all the words in the file up-to two lines even repeated are taken

    lexicon = [lemmatizer.lemmatize(i) for i in lexicon]
    # print(lexicon)
    w_counts = Counter(lexicon)
    # it would be a dict, w_counts = {'the': 300, 'for': 20} dict of the occurring 300 times,
    # for 50 times and so on
    # print(w_counts)
    l2 = []
    for w in w_counts:
        # all words that repeat less than 1000 times and more than 50 times, we take them in
        # if 10 > w_counts[w] > 1:
        if 1000 > w_counts[w] > 50:
            l2.append(w)
    print(len(l2))
    # print(l2)
    return l2


def sample_handling(sample, lexicon, classification):
    featureset = []
    # feature set is a list of list where each element is
    # [
    # [[1 0 1 0 0 1], [1 0]], hot array, each index of the bag of words model, positive sentiment sample
    # [[0 0 1 0 1 1], [0 1]], hot array, each index of the bag of words model, negative sentiment sample
    # ...
    # ]
    with open(sample, 'r') as f:
        contents = f.readlines()
        for l in contents[:hm_lines]:
            current_words = word_tokenize(l.lower())
            current_words = [lemmatizer.lemmatize(i) for i in current_words]
            features = np.zeros(len(lexicon))

            for word in current_words:
                if word.lower() in lexicon:
                    index_value = lexicon.index(word.lower())
                    features[index_value] += 1
            features = list(features)
            featureset.append([features, classification])

    return featureset


def create_feature_sets_and_labels(ppos, nneg, test_size=0.1):
    lexicon = create_lexicon(pos=ppos, neg=nneg)
    # print(lexicon)
    features = []
    features += sample_handling(pos_file, lexicon, [1, 0])
    # print('pos features', features)
    features += sample_handling(neg_file, lexicon, [0, 1])
    # print('neg features', features)
    random.shuffle(features)  # sentdex says this is a really important step

    # does tf.argmax([output]) == tf.argmax([expectations])

    features = np.array(features)
    # print('np array of shuffled features', features)
    # print(len(features))
    # print(test_size*len(features))
    testing_size = int(test_size*len(features))  # nice line of code
    # print(testing_size)
    # [[features, label], [features, label], .... []]
    # [[[1,0,1,1,0,0],[1,0]], [], [], ..... []]

    train_x = list(features[:, 0][:-testing_size])
    train_y = list(features[:, 1][:-testing_size])

    test_x = list(features[:, 0][-testing_size:])
    test_y = list(features[:, 1][-testing_size:])

    return train_x, train_y, test_x, test_y


if __name__ == '__main__':
    train_x, train_y, test_x, test_y = create_feature_sets_and_labels(ppos=pos_file, nneg=neg_file)
    with open('sentiment.pickle', 'wb') as f:
        pickle.dump([train_x, train_y, test_x, test_y], f)
        # dump the return as a list to a pickle file
