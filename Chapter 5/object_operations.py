#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 20:40:14 2020

@author: pratikbhaipatel

Class Numerical Operators

Numeric function --> Called when

object.__add__(self, other) --> self + other
object.__sub__(self, other) --> self - other
ogject.__mul__(self, other) --> self * other
object.__div__(self, other) --> self / other
object.__floordiv__(self, other) --> self // other
object.__pow__(self, other) --> self ** other
object.__and__(self, other) --> self & other
object.__or__(self, other) --> self | other

Also supports in place math operations such as `+=`
(More about this in the data model chapter in the Python documentation)

object.__iadd__(self, other) --> self += other
object.__isub__(self, other) --> self -= other
ogject.__imul__(self, other) --> self *= other
object.__itruediv__(self, other) --> self /= other
object.__ifloordiv__(self, other) --> self //= other
object.__ipow__(self, other) --> self **= other
object.__iand__(self, other) --> self &= other
object.__ior__(self, other) --> self |= other

"""

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "<Point x:{0},y:{1}>".format(self.x, self.y)

    # implement addition
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    # implement subtraction
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    # TODO: implement in-place addition
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

def main():
    print('__main__')
    p1 = Point(10, 20)
    p2 = Point(30, 30)
    print(p1, p2)

    # Add two points
    p3 = p1 + p2
    print(p3)

    # subtract two points
    p4 = p1 - p2
    print(p4)

    # TODO: Perform in-place addition
    p1 += p2
    print(p1)



if __name__ == '__main__':
    main()
