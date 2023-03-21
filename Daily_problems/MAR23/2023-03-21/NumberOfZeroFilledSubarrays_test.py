import pytest
from typing import List
from NumberOfZeroFilledSubarrays_Samu import Solution



def test_zeroFilledSubarray():
    s = Solution()

    assert s.zeroFilledSubarray([1, 0, 0, 0, 2, 0, 0, 3]) == 9
    assert s.zeroFilledSubarray([1, 0, 0, 0, 2, 0, 0, 3, 0]) == 10
    assert s.zeroFilledSubarray([0, 0, 0, 0, 0]) == 15
    assert s.zeroFilledSubarray([1, 2, 3, 4, 5]) == 0
    assert s.zeroFilledSubarray([0, 1, 0, 2, 0, 0, 3, 0, 0, 0]) == 11
    assert s.zeroFilledSubarray([]) == 0
