#!/usr/bin/env python3

from collections import Counter


def isvalid_a(num: int) -> bool:
    """ ensure string has ascending digits
    ensure string has at least one duplicate value
    """
    num = str(num)
    conds = [
        ''.join(sorted(num)) == num,
        len(set(num)) < len(num)
    ]
    return True if all(conds) else False


def isvalid_b(num: int) -> bool:
    """ ensure string has at least one value appear twice
    Note: very unclear from problem wording
    """
    c = Counter(str(num))
    return True if 2 in c.values() else False


def q4a(low: int, high: int) -> int:
    """ count instances in range which satisfy Part A conditions
    """
    return sum(1 for i in range(low, high+1) if isvalid_a(i))


def q4b(low: int, high: int) -> int:
    """ count instances in range which satisfy part A and B conditions
    """
    return sum(1 for i in range(low, high+1) if isvalid_a(i) and isvalid_b(i))


if __name__ == "__main__":

    # tests from instructions
    assert isvalid_a(111111) is True
    assert isvalid_a(223450) is False
    assert isvalid_a(123789) is False

    assert isvalid_a(112233) and isvalid_b(112233) is True
    assert isvalid_a(123444) and isvalid_b(123444) is False
    assert isvalid_a(111122) and isvalid_b(111122) is True

    # answers
    print(q4a(236491, 713787))
    print(q4b(236491, 713787))
