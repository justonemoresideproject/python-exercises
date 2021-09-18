def list_check(lst):
    for ele in lst:
        if isinstance(ele, list) is False:
            return False
    return True
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
