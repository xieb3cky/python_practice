def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    list_copy = []
    for i in lst:
        if i:
            list_copy.append(i)
    return list_copy


    # #solution #2
    # return [i for i in lst if i]
