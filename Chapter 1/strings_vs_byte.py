#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 12:54:06 2020

@author: pratikbhaipatel
"""

def main():
    b = bytes([0x41, 0x42, 0x43, 0x44])
    print(b)
    
    s = "This is a string"
    print(s)
    
    # Try combing b and s
    # print(s + b)
    # The above doesn't work because we need to decode the bytes (even though
    # the bytes contains strings)
    
    s2 = b.decode('utf-8')
    
    print(s+s2)
    
    encodedString = s.encode('utf-8')
    print(encodedString)
    print(b+encodedString)
    
    
    encodedUsing32 = s.encode('utf-32')
    print(encodedUsing32)

if __name__ == "__main__":
    main()
