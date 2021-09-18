def multiple_letter_count(phrase):
    thisDict = {}

    for char in phrase:
        # thisDict[char]+= 1 if char in thisDict else thisDict[char]=1 (Can I make this a one line argument?)
        if char in thisDict:
            thisDict[char]+= 1
        else:
            thisDict[char] = 1
    return thisDict

    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """