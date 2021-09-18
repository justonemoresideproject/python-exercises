def same_frequency(num1, num2):
    lst1 = str(num1)
    lst2 = str(num2)
    dictOne = {}
    dictTwo = {}

    for digit in lst1:
        if digit in dictOne:
            dictOne[digit]+= 1
        else:
            dictOne[digit] = 1
    
    for digit in lst2:
        if digit in dictTwo:
            dictTwo[digit]+= 1
        else:
            dictTwo[digit] = 1

    for digit in dictOne:
        if digit in dictTwo:
            if dictOne[digit] != dictTwo[digit]:
                return False
        else:
            return False

    for digit in dictTwo:
        if digit in dictOne:
            if dictTwo[digit] != dictOne[digit]:
                return False
        else:
            return False
    
    return True
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """