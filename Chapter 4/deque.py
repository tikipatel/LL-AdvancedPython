#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 23:10:39 2020

@author: pratikbhaipatel
"""

import collections
import string


# Deque - double ended queue, pronounced 'deck'

def main():
    print('__main__')
    # initialize a deque with lowercase characters
    d = collections.deque(string.ascii_lowercase)
    
    # deques support the len() function
    print('Item count:', len(d))
    
    # deques can be iterated over
    print('Uppercased the lowercased deque:')
    for elem in d:
        print(elem.upper(), end=', ')
    print('---')
    # manipulate items from either end
    d.pop()
    d.popleft()
    
    d.append(2)
    d.appendleft(1)
    print(d)

    # rotate the deque
    print(d)
    d.rotate(10)
    print(d)


if __name__ == '__main__':
    main()
