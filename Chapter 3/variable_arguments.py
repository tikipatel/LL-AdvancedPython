#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 21:23:45 2020

@author: pratikbhaipatel
"""
    
# Variable amount of parameters
# def addition(*numbers)
# log_message(msgType, msg, *params)

def addition(*args):
    '''
    Returns the sum of all the aruguments passed into the function.

    Parameters
    ----------
    *args : Variable number of numeric types.
        The list of numbers to add up.

    Returns
    -------
    The sum of all the paramters.

    '''
    result = 0
    for arg in args:
        result += arg
    return result



def main():    
    print(addition.__doc__)
    
    # pass different arguments
    print('Using commas to pass args')
    print(addition(5,10,15,20))
    print(addition(1,2,3))
    
    # pas an existing list
    print('Passing in a list')
    nums = [5,10,15,20]
    nums2 = [1,2,3]
    
    print(addition(*nums))
    print(addition(*nums2))

if __name__ == '__main__':
    main()
