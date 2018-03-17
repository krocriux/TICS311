# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 15:07:46 2018

Examples
0)	
    	

{1}

{10}

Returns: 10

Only libraries 1 to 10 must be installed, so the answer is 10.
1)	
    	

{1,101}

{10,110}

Returns: 20

2)	
    	

{1}

{1000}

Returns: 1000

3)	
    	

{1,2,3,4,5}

{6,7,8,9,10}

Returns: 10

In this test case the dependencies have non-empty intersections. One program needs libraries from 1 to 6, another program needs libraries from 2 to 7, and so on. In order to satisfy all dependencies, the package manager will install libraries numbered from 1 to 10, inclusive. Hence, the total number of installed libraries is 10.
4)	
    	

{1,1}

{1,1}

Returns: 1


@author: Cristian
"""
from Intervalos import intervalsMaker

A = [1,2,3,4,5]
B = [6,7,8,9,10]

def install(A, B) :
    intervals_list = intervalsMaker(A, B)
    num_total_libraries = 0
    for interval in intervals_list :
        num_total_libraries += ((interval[1] - interval[0]) + 1)
    return num_total_libraries
        
                    





