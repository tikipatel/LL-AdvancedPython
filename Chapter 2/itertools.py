#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 13:56:20 2020

@author: pratikbhaipatel
"""

import itertools

def testFunction(x):
    return x < 40

def main():
    # Cycle iterator can be used to cycle over a collection
    
    print('Cycle simply starts over with the sequence when it ends')
    seq1 = ['Joe', 'John', 'Mike']
    cycle1 = itertools.cycle(seq1)
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))
    
    # Use count to create a simple counter
    print('Using itertools.count to start a count at a defined start and step')
    count1 = itertools.count(100, 10)
    print(next(count1))
    print(next(count1))
    print(next(count1))
    print(next(count1))
    print(next(count1))
    print(next(count1))
    print(next(count1))
    print(next(count1))
    
    # Accumulate creates an iterator that accumulates values
    print('Using itertools.accumulate to add up some values')
    vals = [10, 20, 30, 40, 50, 40, 30]
    acc_default = itertools.accumulate(vals)
    print(list(acc_default))
    print('By default, it will always add the current + preceeding')
    
    print(
'''
We can provide it a custom function; e.g. use max to keep the max between the 
current and preceeding
'''
)
    acc_max = itertools.accumulate(vals, max)
    print(list(acc_max))    
    
    
    # Use chain to connect sequences together
    print('Chain takes multiple sequences and combines to act as one')
    x = itertools.chain('ABCD', '1234')
    print(list(x))
    
    # dropwhile and takewhile will return valus until a certain condition is
    # met
    
    print('dropwhile')
    print(list(itertools.dropwhile(testFunction, vals)))
    print('takewhile')
    print(list(itertools.takewhile(testFunction, vals)))
    
    
if __name__ == '__main__':
    main()