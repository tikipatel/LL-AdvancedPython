"""
Set Comprehensions
"""


def main():
    print('__main__')
    c_temps = [5, 10, 12, 14, 10, 23, 41, 30, 12, 24, 18, 12, 29]
    f_temps_comprehension = [(t*9/5)+32 for t in c_temps]
    print('f temps array:', f_temps_comprehension)
    f_temps_set_comprehension = {(t*9/5)+32 for t in c_temps}
    print('f temps set:', f_temps_set_comprehension)

    # build a set of unique Fahrenheit temperatures

    # build a set from an input source
    temp_string = 'The quick brown fox jumped over the lazy dog'
    uppercase_chars = {c.upper() for c in temp_string}
    print(uppercase_chars)
    uppercase_chars_exclude_space = {c.upper() for c in temp_string if not c.isspace()}
    print(uppercase_chars_exclude_space)


if __name__ == '__main__':
    main()