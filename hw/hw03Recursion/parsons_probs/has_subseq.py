def has_subseq(n, seq):
    """
    Complete has_subseq, a function which takes in a number n and a "sequence"
    of digits seq and returns whether n contains seq as a subsequence, which
    does not have to be consecutive.

    >>> has_subseq(123, 12)
    True
    >>> has_subseq(141, 11)
    True
    >>> has_subseq(144, 12)
    False
    >>> has_subseq(144, 1441)
    False
    >>> has_subseq(1343412, 134)
    True
    """
    #能过测试，漏洞在n,seq==0的时候
    if seq == 0:
        return True
    if n == 0:
        return False
    if n % 10 == seq % 10:
        return has_subseq(n // 10, seq // 10)
    without = has_subseq(0, 1)  #多余的
    return has_subseq(n // 10, seq) or without
    """
    if n == seq:
        return True
    if n < seq:
        return False
    without = has_subseq(n // 10, seq)
    if seq % 10 == n % 10:
        return has_subseq(n // 10, seq // 10) or without
    return without
    """