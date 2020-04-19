#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 12:52:54 2020

@author: pratikbhaipatel
"""

from string import Template

# Template strings
def main():
    str1 = "You're watching {0} by {1}".format(
        "Advanced Python", 
        "Joe Marini"
        )
    print("Created by String.format(): " + str1)
    
    # Create a template with placeholders
    template = Template(
        "You're watching ${title} by ${author}"
        )
    
    str2 = template.substitute(title="Advanced Python", author="Joe Marini")
    print("Created by Template: " + str2)
    
    # Use substitude method with a dictionary
    authorData = {
        "author": "Joe Marini",
        "title": "Advanced Python",
        }
    str3 = template.substitute(authorData)
    
    print("Created by `template.substitue(`mapping`)`: " + str3)
    
    
if __name__ == "__main__":
    main()


