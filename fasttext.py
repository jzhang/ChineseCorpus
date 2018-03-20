#!/usr/bin/env python3

# -*- coding=utf-8 -*-

from gensim.models import KeyedVectors

if __name__ == '__main__':
    model = KeyedVectors.load_word2vec_format('/home/jzh/corpus/fasttext/wiki.zh.vec')
    print(model.most_similar("夏天"))
    print(model.similarity("夏天", "冬天"))    