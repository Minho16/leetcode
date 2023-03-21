import pytest
from Number_of_Zero_Filled_Subarrays_Minho import Solution


@pytest.mark.parametrize("nums, expected", [
    ([1, 0, 1, 0, 0, 1, 0], 5),
    ([0, 0, 0, 1, 0, 0, 0], 12),
    ([1, 1, 1, 1, 1, 1], 0),
    ([0, 1, 0, 1, 0, 1, 0], 4),
    ([1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0], 19),
])
def test_zeroFilledSubarray(nums, expected):
    solution = Solution()
    result = solution.zeroFilledSubarray(nums)
    assert result == expected
