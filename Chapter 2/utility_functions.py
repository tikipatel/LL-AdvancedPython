# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 12:52:54 2020

@author: pratikbhaipatel
"""

def main():
    print("*** Python's Built-In Utility Functions ***")
    # Use any() and all() to test sequences for boolean values
    list_1 = [1, 2, 3, 0, 5, 6]
    
    # any will return true if any of the sequence values is true
    print(any(list_1)) # prints 'True'
    
    # all will return true only if all values are true
    print(all(list_1)) #prints 'False'
    
    # min and max will return the minimum and maximum values in a sequence
    print("min: ", min(list_1))
    print("max: ",  max(list_1))
    
    # sum() will sum up all the values in a sequence
    print("sum: ", sum(list_1))
    
if __name__ == "__main__":
    main()