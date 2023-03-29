import pytest
from typing import List
from MinimumPathSum_Samu import Solution

@pytest.mark.parametrize("input_grid, expected_output", [
    ([[1, 3, 1], [1, 5, 1], [4, 2, 1]], 7),
    ([[1, 2, 3], [4, 5, 6]], 12),
    ([[1]], 1),
    ([[1, 2], [1, 2]], 4),
    ([[1, 0, 0], [0, 1, 0], [0, 0, 1]], 2)
])
def test_minPathSum(input_grid: List[List[int]], expected_output: int):
    solution = Solution()
    result = solution.minPathSum(input_grid)
    assert result == expected_output
