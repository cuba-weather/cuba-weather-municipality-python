def distance(s1 : str, s2 : str) -> int:
    '''
    Implementation of Damerau-Levenshtein distance with transposition (also
    sometimes calls unrestricted Damerau-Levenshtein distance).

    It is the minimum number of operations needed to transform one string into
    the other, where an operation is defined as an insertion, deletion, or
    substitution of a single character, or a transposition of two adjacent
    characters.
    '''

    d : dict = {}
    
    for i in range(-1, len(s1) + 1):
        d[i, -1] = i + 1
    for j in range(-1, len(s2) + 1):
        d[-1, j] = j + 1
    for i, cs1 in enumerate(s1):
        for j, cs2 in enumerate(s2):
            cost = int(cs1 != cs2)
            d[i, j] = min(d[i - 1, j] + 1, d[i, j - 1] + 1, d[i - 1, j - 1] + cost)
            if not i or not j:
                continue
            if cs1 != cs2:
                continue
            d[i, j] = min(d[i, j], d[i - 2, j - 2] + cost)
    return d[len(s1) - 1, len(s2) - 1]
