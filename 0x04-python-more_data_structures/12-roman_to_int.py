#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is not None or type(roman_string) is str:
        r_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
                  'M': 1000}
        integer = 0
        for i in range(len(roman_string)):
            if roman_string[i] in r_dict:
                integer += r_dict[roman_string[i]]
                if i > 0 and r_dict[roman_string[i]] > r_dict[roman_string[i - 1]]:
                    integer -= 2 * r_dict[roman_string[i - 1]]
            else:
                return 0
        return integer
    return 0
