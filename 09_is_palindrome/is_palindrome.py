def is_palindrome(phrase):
    thisPhrase = phrase.replace(' ', '')
    for x in range(0, len(thisPhrase) - 1):
        if thisPhrase[x].upper() != thisPhrase[-x - 1].upper():
            return False
    return True
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
