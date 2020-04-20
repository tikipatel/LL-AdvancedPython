#!/usr/bin/env python3
"""
Created on Sun Apr 19 21:28:33 2020

@author: pratikbhaipatel
"""


class Employee():
    def __init__(self, first_name, last_name, level, years_of_service):
        self.first_name = first_name
        self.last_name = last_name
        self.level = level
        self.seniority = years_of_service

    # TODO: implement comparison functions by emp level
    def __ge__(self, other):
        if self.level == other.level:
            return self.seniority >= other.seniority
        return self.level >= other.level

    def __gt__(self, other):
        if self.level == other.level:
            return self.seniority > other.seniority
        return self.level > other.level

    def __lt__(self, other):
        if self.level == other.level:
            return self.seniority < other.seniority
        return self.level < other.level

    def __le__(self, other):
        if self.level == other.level:
            return self.seniority <= other.seniority
        return self.level <= other.level

    def __eq__(self, other):
        return self.level == other.level



def main():
    print('__main__')
    # define some employees
    dept = [
        Employee("Tim", "Sims", 5, 9),
        Employee("John", "Doe", 4, 12),
        Employee("Jane", "Smith", 6, 6),
        Employee("Rebbecca", "Robinson", 5, 13),
        Employee("Tyler", "Durden", 5, 12),
    ]

    # Who's more senior?
    # is tim more senior than jane?
    print(dept[0] > dept[2])
    # is tyler less senior than rebbecca?
    print(dept[4] < dept[3])

    # sort the items
    sorted_employees = sorted(dept)
    for employee in sorted_employees:
        print(employee.first_name, employee.last_name)


if __name__ == '__main__':
    main()
