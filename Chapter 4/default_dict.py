#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 22:04:27 2020

@author: pratikbhaipatel
"""

# using defaultdict
# import collections
from collections import defaultdict

def main():
    print('__main__')
    fruits = ['apple', 'pear', 'orange', 'banana',
              'apple', 'grape', 'banana', 'banana',
              ]
    
    print('not using defaultdict')
    # use a dictionary to count each element
    fruit_counter = {}
    
    # count the elements in the list
    for fruit in fruits:
        if fruit in fruit_counter.keys():
            fruit_counter[fruit] += 1
        else:
            fruit_counter[fruit] = 1

    # print the result
    for (k, v) in fruit_counter.items():
        print(k, ':', v)
        
    
    print('using defaultdict')
    # use a dictionary to count each element
    fruit_counter = defaultdict(int)
    
    # count the elements in the list
    for fruit in fruits:
        fruit_counter[fruit] += 1

    # print the result
    for (k, v) in fruit_counter.items():
        print(k, ':', v)
        
    # we can use lambdas to create a default dict
    print('defaultdict with a lambda to initialize non-existent keys')
    custom_counter = defaultdict(lambda: 100)
    print(custom_counter['hello'])
    
    
if __name__ == '__main__':
    main()
    