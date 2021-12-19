def roman_to_arabic(numerals):
    reference = {'m': 1000, 'd': 500, 'c': 100, 'l': 50, 'x': 10, 'v': 5, 'i': 1}
    conversion = 0
    for i in range(len(numerals)):
        if numerals[i].lower() == 'v' and numerals[i - 1] == 'i':
            conversion += 3
        elif numerals[i].lower() == 'x' and numerals[i - 1] == 'i':
            conversion += 8
        elif numerals[i].lower() == 'l' and numerals[i - 1] == 'x':
            conversion += 30
        else:
            conversion += reference[numerals[i]]
    return conversion
