def flip_case(phrase, to_swap):
    newPhrase = ''
    for char in phrase:
        if char.upper() == to_swap.upper():
            if char.isupper():
                newPhrase+=char.lower()
            else:
                newPhrase+=char.upper()
        else:
            newPhrase+=char
    return newPhrase

    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
