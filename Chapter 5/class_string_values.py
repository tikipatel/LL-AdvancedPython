#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 17:47:52 2020

@author: pratikbhaipatel

Class String Functions

function --> called when

object.__str__(self) --> str(object), print(object), '{0}'.format(object)
object.__repr__(self) --> repr(object)
object.__format__(self, format_spec) --> format(object, format_spec)
object.__bytes__(self) --> bytes(object)
"""


class Person():
    def __init__(self):
        self.first_name = 'Pratik'
        self.last_name = 'Patel'
        self.age = 25

    # TODO: use __repr__ to create a string useful for debugging
    def __repr__(self):
        return ''''<-- Person Class--
first_name: {0}
last_name: {1}
age: {2}
-- Person Class -->
'''.format(self.first_name, self.last_name, self.age)

    # TODO: use str for a more human-redable string
    def __str__(self):
        return '{0} {1} is {2}'.format(
            self.first_name,
            self.last_name,
            self.age
            )

    def __bytes__(self):
        val = '{0} {1} is {2}'.format(
            self.first_name,
            self.last_name,
            self.age
            )
        return bytes(val.encode('utf-8'))


def main():
    print('** Class String Functions **')

    # create a new Person object
    person1 = Person()
    print(person1)

    # use different Python functions to convert it to a string
    print('Using repr(object):', repr(person1))
    print('Using str(object):', str(person1))
    print('Using \'{$0}\'.format(ojbect):', '{0}'.format(person1))
    print('Using bytes(object):', bytes(person1))


if __name__ == '__main__':
    main()
