#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 22:31:27 2020

@author: pratikbhaipatel
"""

from collections import OrderedDict, namedtuple


def main():
    # list of sports teams with wins and losses
    ScoreTracker = namedtuple('Score', 'wins losses')
    sports_teams = [
        ('Royals', ScoreTracker(18, 12)),
        ('Rockets', ScoreTracker(24, 6)),
        ('Cardinals', ScoreTracker(20, 10)),
        ('Dragons', ScoreTracker(22, 8)),
        ('Kings', ScoreTracker(15, 15)),
        ('Chargers', ScoreTracker(20, 10)),
        ('Jets', ScoreTracker(16, 14)),
        ('Warriors', ScoreTracker(25, 5)),
        ]
    sorted_teams = sorted(
        sports_teams,
        key=lambda t: t[1].wins,
        reverse=True
        )
    print(sorted_teams)
    sports_teams = [
        ('Royals', (18, 12)),
        ('Rockets', (24, 6)),
        ('Cardinals', (20, 10)),
        ('Dragons', (22, 8)),
        ('Kings', (15, 15)),
        ('Chargers', (20, 10)),
        ('Jets', (16, 14)),
        ('Warriors', (25, 5)),
        ]

    # sort the teams by number of wins
    sorted_teams = sorted(
        sports_teams,
        key=lambda t: t[1][0],
        reverse=True
        )
    print(sorted_teams)

    # create an ordered dict
    teams = OrderedDict(sorted_teams)
    print(teams)

    # use popitem to remove top item
    tm, wl = teams.popitem(False)
    print('Top Team:', tm, wl)
    for i, team in enumerate(teams, start=1):
        print(i, team)
        if i == 4:
            break

    # test for equality
    a = OrderedDict({'a': 1, 'b': 2, 'c': 3})
    b = OrderedDict({'a': 1, 'b': 2, 'c': 3})
    print('is a equal to b:', a == b)

    a = OrderedDict({'a': 1, 'b': 2, 'c': 3})
    b = OrderedDict({'a': 1, 'c': 3, 'b': 2})
    # False because order is not the same
    print('is a equal to b:', a == b)

    ordered_a = OrderedDict({'a': 1, 'b': 2, 'c': 3})
    regular_b = {'a': 1, 'c': 3, 'b': 2}
    # True because OrderedDict when compared to a regular dict, order doesn't
    # matter
    print('is ordered_a equal to regular_b:', ordered_a == regular_b)


if __name__ == '__main__':
    main()
