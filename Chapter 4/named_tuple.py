#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 21:58:28 2020

@author: pratikbhaipatel
"""

# Using named tuple
import collections


def main():
    print('__main__')

    # create Point namedtuple
    Point = collections.namedtuple('Point', 'x y')
    p1 = Point(10, 20)
    p2 = Point(30, 44)

    print(p1, p2)

    print('p1.x:', p1.x)

    # use _replace to create new instance
    p1 = p1._replace(x=100)
    print(p1)


if __name__ == '__main__':
    main()
