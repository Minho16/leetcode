import pytest
from typing import List
from ReducingNodes_Samu import Solution

def test_maxSatisfaction():
    solution = Solution()

    test_cases = [
        ([-1, -8, 0, 5, -9], 14),
        ([4, 3, 2], 20),
        ([-1, -4, -5], 0),
        ([-2, 5, -1, 0, 3, -3], 35),
    ]

    for satisfaction, expected_output in test_cases:
        assert solution.maxSatisfaction(satisfaction) == expected_output
