#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 13:05:02 2020

@author: pratikbhaipatel
"""

def main():
    # Define list of day abbreviations in English and French
    days_en = ['Sun', "Mon", "Tue", 'Wed', 'Thu', 'Fri', 'Sat', 'Non-existent']
    days_fr = ['Dim', 'Lun', 'Mar', 'Mer', 'Jue', 'Ven', 'Sam']
    
    print('English days of the week: ', days_en)
    print('French days of the week: ', days_fr)
    
    # Use iter to create an iterate over a collection
    print('Use iter to create an iterate over a collection')
    i = iter(days_en)
    print(next(i))
    print(next(i))
    print(next(i))
    print(next(i))
    
    print('Using iter function and a sentinel')
    with open('testfile.txt', 'r') as fp:
        for line in iter(fp.readline, ''):
            print(line)
    
    # iterate over days
    print('Printing days with iteration type `for x in seq`')
    for day in days_en:
        print(day)
    
    print('Printing using a not-so-good way to get index')
    for idx in range(len(days_en)):
        print(idx, days_en[idx])
    
    # using enumerate -- takes a collection along with an optional starting 
    # value and it returns a tuple that contains the index value of the current
    # item along with the item in a collection
    
    print('Using the enumerate function')
    for index, value in enumerate(days_en, start=1):
        print(index, value)
        
    # using the zip function to combine sequences -- useful when wanting to
    # enumerate over multiple sequences at the same time. zip takes n-number
    # of sequences and combines them into a single iterator
    print('Using zip')
    for days in zip(days_en, days_fr):
        print(days)
        
    print('Using enumerate + zip')
    for index, days in enumerate(zip(days_en, days_fr), start=1):
        print(index, days[0], '=', days[1], 'in French')
    
    print('''
If the two sequences aren\'t of the same lenght, then it terminates 
when the shortest sequence ends
'''
          )
    
    

if __name__ == "__main__":
    main()