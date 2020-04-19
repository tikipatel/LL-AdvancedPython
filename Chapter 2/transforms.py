#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 13:36:24 2020

@author: pratikbhaipatel

Python has become popular among data scientists and others who need to work 
with large sets of data. This is no accident because the Python standard
library provides built-in functions for transforming sets of data.
"""

def odds(x):
    if x % 2 == 0:
        return False
    return True

def lowers(x):
    if x.isupper():
        return False
    return True

def square(x):
    return x**2

def grade(x):
    if x >= 90:
        return 'A'
    if x >= 80:
        return 'B'
    if x >= 70:
        return 'C'
    if x >= 65:
        return 'D'
    return 'F'


def main():
    print("Transforms!")
    # define some sample sequences on which to operate
    nums = (1, 8, 4, 5, 13, 26, 381, 410, 58)
    chars = "abcDeFGHiJklmnoP"
    grades = (81, 89, 94, 78, 61, 66, 99, 74)
    
    # use filter to remove items from a list
    print('Using filter to remove items from a list')
    odd_numbers = list(filter(odds, nums))
    print(odd_numbers) # Prints [1, 5, 13, 381]
    
    # using filter on non-numeric sequence
    print('Using filter with non-numeric sequences')
    lower_characters = list(filter(lowers, chars))
    print(lower_characters)
    
    # Map creates an iterator that takes one or more sequences of values
    # and produces a new sequence by applying a given function to each valu
    # in the original sequences
    
    print('Squared values of nums using the mapping function')
    squares = list(map(square, nums))
    print(squares)
    
    print('Letter grades using mapping on grades')
    letter_grades = list(map(grade, grades))
    print(letter_grades)
    
    
    
    
    
if __name__ == "__main__":
    main()