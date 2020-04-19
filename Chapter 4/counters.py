#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 22:15:01 2020

@author: pratikbhaipatel
"""


from collections import Counter

def main():
    print('__main__')
    # list of students in class 1
    class1 = ['bob', 'chad', 'darcy', 'frank', 'hannah',
              'kevin','becky', 'james', 'james', 'melanie', 'penny', 'steve'
              ]
    
    class2 = ['bill', 'barry', 'cindy', 'debby', 'frank', 'gabby',
              'kelly', 'james', 'joe', 'sam', 'tara', 'ziggy'
              ]
    
    # create counter for class1 and class2
    c1 = Counter(class1)
    c2 = Counter(class2)
    
    print(c1)
    print(c2)
    
    # how many in class1 named james?
    print('number of james in class 1: ', c1['james'])

    # how many total students in clss 1?
    print(sum(c1.values()), 'students in class 1')   
    
    # combine the two classes    
    c1.update(class2)
    print(sum(c1.values()), 'students in class 1')
    
    # most common
    print(c1.most_common(3))
    
    # subtract / separate classes
    c1.subtract(c2)
    print(c1)
    print(c1.most_common(3))
    
    # most common between the two classes
    print(c1 & c2)
    
    
if __name__ == '__main__':
    main()