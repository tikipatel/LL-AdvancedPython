# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Demo file for Spyder Tutorial
# Hans Fangohr, University of Southampton, UK

def hello():
    """Print "Hello World" and return None."""
    print("Hello World")

# Main program starts here
hello()






# Two constants -- False and None evaluate to false and any "0" values
# Numerics : 0, 0.0, 0j
# Decimal(0), Fraction(0, x)
# Empty sequences / collections: ", (), []. {}
# Empty sets and ranges: set(), range(0)

# Overriding __bool__ or __len__ to return something else might also give
# false

class alwaysFalse:
    def __bool__(self):
        return False
    
    def __len__(self):
        return 0

print(bool(alwaysFalse()))
print(len(alwaysFalse()))







    
    

    
    
    
    
