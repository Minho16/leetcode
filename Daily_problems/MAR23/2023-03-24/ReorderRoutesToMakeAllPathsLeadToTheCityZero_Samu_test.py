import pytest
from typing import List

# Assuming the Solution class is in a file named solution.py
from ReorderRoutesToMakeAllPathsLeadToTheCityZero_Samu import Solution

# Fixture for creating a Solution object
@pytest.fixture
def solution():
    return Solution()

# Test cases
def test_minReorder(solution):
    assert solution.minReorder(6, [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]) == 3
    assert solution.minReorder(5, [[1, 0], [1, 2], [3, 2], [3, 4]]) == 2
    assert solution.minReorder(3, [[1, 0], [2, 0]]) == 0
    assert solution.minReorder(4, [[0, 1], [2, 3], [2, 1]]) == 2
