def vowel_count(phrase):
    vowels = 'aeiou'
    thisDict = {}
    for letter in phrases:
        if letter.lower() in vowels:
            if letter in thisDict:
                thisDict[letter.lower()] = 1
            else
                thisDict[letter.lower()]+=1
    return thisDict
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """