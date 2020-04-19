#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 21:44:12 2020

@author: pratikbhaipatel
"""

# Demonstrate the use of keyword-only arguments

def myFunction(arg1, arg2, *, supressExceptions=False):
    pass


def main():
    print('__main__')
    myFunction(1, 2, supressExceptions=True)
    

if __name__ == '__main__':
    main()