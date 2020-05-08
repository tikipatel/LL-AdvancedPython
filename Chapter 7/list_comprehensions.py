"""
List Comprehensions
"""


def subtractOne(x):
    return x - 1


def main():
    print('__main__')

    # define two lists of numbers
    evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    odds = list(map(subtractOne, evens))
    print('evens:', evens)
    print('ods:', odds)

    # perform a mapping and filter function on a list
    # doing things the old way, using a lambda
    evens_squared = list(map(lambda e: e ** 2, evens))
    print('evens squared:', evens_squared)

    filtered_evens_squared = list(
        map(lambda e: e ** 2, filter(lambda e: 4 < e < 16, evens))
    )
    print('filtered evens squared:', filtered_evens_squared)

    # derive a new list of numbers from a given list
    evens_squared_comprehension = [e ** 2 for e in evens]
    print('evens_squared_comprehension:', evens_squared_comprehension)

    # limit the items operated on with a predicate condition
    filtered_evens_squared_comprehension = [o ** 2 for o in odds if 3 < o < 17]
    print('filtered_evens_squared_comprehension:', filtered_evens_squared_comprehension)


if __name__ == '__main__':
    main()