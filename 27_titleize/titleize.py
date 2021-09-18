def titleize(phrase):
    count = 1
    newPhrase = []
    for letter in phrase:
        if count == 1:
            newPhrase.append(letter.upper())
            count-=1
        elif letter == ' ':
            count+=1
            newPhrase.append(' ')
        else:
            newPhrase.append(letter.lower())
    return "".join(newPhrase)

    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
