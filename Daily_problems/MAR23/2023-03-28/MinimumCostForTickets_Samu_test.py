import pytest
from typing import List
from MinimumCostForTickets_Samu import Solution

@pytest.mark.parametrize("days, costs, expected_output", [
    ([1, 4, 6, 7, 8, 20], [2, 7, 15], 11),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15], 17),
    ([4, 5, 9, 11, 14, 16, 17, 19, 21, 22, 24], [1, 4, 18], 10),
    ([1, 4, 6, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21, 22, 23, 27, 28], [3, 13, 45], 44)
])

def test_minPathSum(days: List[int], costs: List[int], expected_output: int):
    solution = Solution()
    result = solution.mincostTickets(days, costs)
    assert result == expected_output
