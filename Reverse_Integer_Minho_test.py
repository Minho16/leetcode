from Reverse_Integer_Minho import Solution


def test_reverse():
    s = Solution()

    # Test for positive integers
    assert s.reverse(123) == 321
    assert s.reverse(120) == 21
    assert s.reverse(1) == 1

    # Test for negative integers
    assert s.reverse(-123) == -321
    assert s.reverse(-120) == -21
    assert s.reverse(-1) == -1

    # Test for 0
    assert s.reverse(0) == 0

    # Test for overflow
    assert s.reverse(2147483647) == 0
    assert s.reverse(-2147483648) == 0
