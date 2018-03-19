# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 10:59:45 2018

@author: Cristian
"""
s = [1, 2, 4]
t = [3, 4, 6]

def count(s, t) :
    index_rabbits_now = []
    counter = 0
    for i in range(0, max(t) + 1) : 
        for j in range(len(s)) :
            if s[j] == i :
                index_rabbits_now.append(j)
        for j in range(len(t)) :
            if t[j] == i :
                index_rabbits_now.remove(j)
                counter += len(index_rabbits_now)
    return counter

def count2(s, t) :
    n = len(s)
    count = 0
    for conejo1 in range(n) :
        for conejo2 in range(conejo1 + 1, n) :
            if (t[conejo1] >= s[conejo2]) and (s[conejo1] <= t[conejo2]):
                count += 1
    return count

def count3(s, t) :
    n = len(s)
    count = 0
    for conejo1 in range(n) :
        for conejo2 in range(conejo1 + 1, n) :
            if se_conocen(conejo1, conejo2, s, t) :
                count += 1
    return count

def se_conocen(c1, c2, s, t) :
    return not (t[c1] < s[c2] or t[c2] < s[c1])




