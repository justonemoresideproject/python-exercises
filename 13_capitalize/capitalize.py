def capitalize(phrase):
    return phrase.replace(phrase[0], phrase[0].upper())
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """