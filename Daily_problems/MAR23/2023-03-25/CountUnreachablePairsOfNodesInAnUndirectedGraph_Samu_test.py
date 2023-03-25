import pytest
from typing import List

from CountUnreachablePairsOfNodesInAnUndirectedGraph_Samu import Solution

# Fixture for creating a Solution object
@pytest.fixture
def solution():
    return Solution()

# Test cases
def test_countPairs(solution):
    assert solution.countPairs(5, [[0, 1], [1, 2], [3, 4]]) == 6
    assert solution.countPairs(4, [[0, 1], [1, 2], [2, 3]]) == 0
    assert solution.countPairs(6, [[0, 1], [1, 2], [2, 3], [4, 5]]) == 8
    assert solution.countPairs(5, [[0, 1], [1, 2], [2, 3], [3, 4]]) == 0
