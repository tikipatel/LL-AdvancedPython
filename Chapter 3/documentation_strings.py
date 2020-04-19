#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 20:51:44 2020

@author: pratikbhaipatel
"""

def myFunction(arg1, arg2=None):
    '''myFunction(arg1, arg2=None) --> Doesn't really do anything, just prints.

    Parameters
    ----------
    arg1 : String
        String type that would be printed.
    arg2 : TYPE, optional
        DESCRIPTION. The default is None.

    Returns
    -------
    None.

    '''
    

# Docstrings should always be in triple-quotes
# First line should be a summary sentence of functionality
# Modules: list important classes, functions, and exceptions
# Classes: list import methods


# Functions:
    # list the parameters and explain each -- one per line
    # PEP 257

def main():
    print(myFunction.__doc__)
    
if __name__ == '__main__':
    main()