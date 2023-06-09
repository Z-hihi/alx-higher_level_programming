#!/usr/bin/python3
def roman_to_int(roman_string):
    D = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "M": 1000, "D": 500}

    if (roman_string and isinstance(roman_string, str)):
        S = 0

        for i in range(len(roman_string)):
            if i > 0:
                if D[roman_string[i - 1]] < D[roman_string[i]]:
                    S = S + D[roman_string[i]] - (2 * D[roman_string[i - 1]])
                else:
                    S = S + D[roman_string[i]]
            else:
                S = S + D[roman_string[i]]
        return S
    else:
        return 0
