def compact(lst):
    newLst = []
    for char in lst:
        if char:
            newLst.append(char)
    return newLst
        
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """