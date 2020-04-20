#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 23:25:49 2020

@author: pratikbhaipatel
"""

from enum import Enum, unique, auto

# Define enumerations using the Enum base class


@unique
class Fruit(Enum):
    APPLE = 1
    BANANA = 2
    ORANANGE = 3
    TOMATO = 4
    # APPLE = 5 (Can't have duplicate names (key))
    # Can have duplicate values
    # GRANNY_SMITH = 1
    PEAR = auto()

    # can have unique values by importing unique decorator.

    # use auto from enum for automatically assigning values


def main():
    print('__main__')

    # enums have human-readable values and types
    print(Fruit.APPLE)
    print(type(Fruit.APPLE))
    print(repr(Fruit.APPLE))

    # enums have name and value properties
    print(Fruit.APPLE.name, Fruit.APPLE.value)

    # print the auto-generated values
    print(Fruit.PEAR.name, Fruit.PEAR.value)

    # enums are hashable - can be used as keys
    my_fruits = {}
    my_fruits[Fruit.BANANA] = 'Come Mr. Tally-man'
    print(my_fruits[Fruit.BANANA])


if __name__ == '__main__':
    main()
