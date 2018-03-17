# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 20:37:57 2018

@author: Cristian
"""

dictionary = ["cat", "cab", "lab"]
candidate = "dab"

def selectWord(dictionary, candidate):
    most_similar_index = 0
    max_number_matches = 0
    for word in dictionary:
        matches = 0
        for i in range(len(word)):
            if word[i] == candidate[i]:
                matches += 1
        if matches > max_number_matches:
            max_number_matches = matches
            most_similar_index = dictionary.index(word)
    if max_number_matches == 0:
        return -1
    else:
        return most_similar_index
    