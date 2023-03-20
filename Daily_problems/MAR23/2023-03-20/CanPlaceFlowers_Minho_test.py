from CanPlaceFlowers_Minho import Solution
import pytest


# Test cases
@pytest.mark.parametrize(
    "flowerbed, flowers, expected",
    [
        ([1, 0, 0, 0, 1], 1, True),
        ([1, 0, 0, 0, 1], 2, False),
        ([1, 0, 0, 0, 1], 0, True),
        ([1, 0, 0, 0, 1], 3, False),
    ],
)
def test_can_place_flowers(flowerbed, flowers, expected):
    sol = Solution()
    result = sol.canPlaceFlowers(flowerbed=flowerbed, n=flowers)
    assert result == expected
