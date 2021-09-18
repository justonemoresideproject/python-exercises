def mode(nums):
    thisDict = {}
    for char in nums:
        if char in thisDict:
            thisDict[char]+= 1
        else:
            thisDict[char] = 1
    highestKey = -1
    for key in thisDict:
        if highestKey == -1:
            highestKey = key
        elif thisDict[highestKey] < thisDict[key]:
            highestKey = key
    return highestKey

    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
