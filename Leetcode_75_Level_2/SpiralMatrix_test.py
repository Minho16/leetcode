from SpiralMatrix_Samu import Solution
import pytest


class TestSolution:
    # Pytest fixture option 'saves' the Class Solution to be used in all our test
    @pytest.fixture
    def solution(self):
        return Solution()

    # Pytest mark parametrize help us to initialize the input and expected output on a function to then use the assert method
    @pytest.mark.parametrize(
        "matrix, spiral",
        [
            ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5]),
            (
                [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
                [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
            ),
            (
                [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],
                [1, 2, 3, 6, 9, 12, 11, 10, 7, 4, 5, 8],
            ),
        ],
    )
    def testSpiralOrder(self, solution, matrix, spiral):
        assert solution.spiralOrder(matrix) == spiral
