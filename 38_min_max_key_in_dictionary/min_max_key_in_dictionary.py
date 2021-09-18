def min_max_keys(d):
    greater = None
    lesser = None
    for key in d:
        if greater == None:
            greater = key
            lesser = key
        if key > greater:
            greater = key
        if key < lesser:
            lesser = key
    return (lesser, greater)
    """Return tuple (min-keys, max-keys) in d.

        >>> min_max_keys({2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'})
        (1, 10)

    Works with any kind of key that can be compared, like strings:

        >>> min_max_keys({"apple": "red", "cherry": "red", "berry": "blue"})
        ('apple', 'cherry')
    """