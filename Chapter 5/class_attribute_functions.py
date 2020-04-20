#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 18:12:25 2020

@author: pratikbhaipatel

Attribute function --> Called when

(called every time UNCONDITIONALLY; called by Python when it looks up methods
 in your class.)
object.__getattribute__(self, attr) --> object.attr

(only when requested attribute can't be found on the object')
object.__getattr__(self, attr) --> object.attr

object.__setattr__(self, attr, val) --> object.attr = val
object.__delattr__(self) --> del object.attr
object.__dir__(self) --> dir(object)
"""


class CustomColor():
    def __init__(self):
        self.red = 50
        self.green = 75
        self.blue = 100
        self.alpha = 43
        
    # Use __getattr__ to dynamically return a value
    def __getattr__(self, attr):
        if attr == 'rgb_color':
            return (self.red, self.green, self.blue)
        elif attr == 'hex_color':
            return '#{0:02x}{1:02x}{2:02x}'.format(
                self.red, self.green, self.blue
                )
        else:
            raise AttributeError

    # use __setattr__ to dynamically set a value
    def __setattr__(self, attr, value):
        if attr == 'rgb_color':
            self.red = value[0]
            self.green = value[1]
            self.blue = value[2]
        else:
            super().__setattr__(attr, value)

    # use dir to list avalable properties
    def __dir__(self):
        return ('red', 'green', 'blue', 'alpha', 'rgb_color', 'hex_color')


def main():
    print('** Class Attribute Functions **')
    
    # create an instance of CustomColor
    custom_color = CustomColor()
    
    # print the value of a computed property
    print('RGB color:', custom_color.rgb_color)
    print('Hex color:', custom_color.hex_color)

    # set the value of a computed property
    custom_color.rgb_color = (12, 52, 255)
    print('RGB color:', custom_color.rgb_color)
    print('Hex color:', custom_color.hex_color)        
    
    # access a regular attribute
    print(custom_color.red, custom_color.blue)
    
    # list the available attributes
    print(dir(custom_color))
    
    x = 'hello'
    print(dir(x))
    
    

if __name__ == '__main__':
    main()
