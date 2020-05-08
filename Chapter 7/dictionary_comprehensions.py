"""
Dictionary Comprehensions
"""


def subtractOne(x):
    return x - 1


def main():
    print('__main__')
    c_temps = [0, 12, 34, 100]

    # build a dictionary using comprehension
    temp_dict = {t: (t * 9 / 5) + 32 for t in c_temps}
    print('temp dict:', temp_dict)
    print('value of 12:', temp_dict[12])
    # only temps less than 100
    predicated_temp_dict = {t: (t * 9 / 5) + 32 for t in c_temps if t < 100}
    print('predicated temp dict:', predicated_temp_dict)
    # print('value of 100:', predicated_temp_dict[100]) # this will throw the KeyError

    # merge 2 dictionaries using comprehension
    # teams with last name and jersey number
    team_1 = {'Jones': 24, 'Jameson': 18, 'Smith': 58, 'Burns': 7}
    team_2 = {'White': 12, 'Mack': 88, 'Pierce': 4}

    # generally limit to 2 comprehensions
    combined_team = {k: v for team in (team_1, team_2) for k, v in team.items()}
    print(combined_team)


if __name__ == '__main__':
    main()
