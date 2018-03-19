# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 13:56:23 2018

@author: Cristian
"""

def count2(s, t) :
    n = len(s)
    count = 0
    for conejo1 in range(n) :
        for conejo2 in range(conejo1 + 1, n) :
            if (t[conejo1] >= s[conejo2]) and (s[conejo1] <= t[conejo2]):
                count += 1
    return count