from WhereWillTheBallFall_Samu import Solution


class TestSolution:
    def test1(self):
        grid = [
            [1, 1, 1, -1, -1],
            [1, 1, 1, -1, -1],
            [-1, -1, -1, 1, 1],
            [1, 1, 1, 1, -1],
            [-1, -1, -1, -1, -1],
        ]
        # create an instance of the Solution class
        solution = Solution()

        # call the detectCycle function
        result = solution.findBall(grid)

        assert result == [1, -1, -1, -1, -1]

    def test2(self):
        grid = [[-1]]
        # create an instance of the Solution class
        solution = Solution()

        # call the detectCycle function
        result = solution.findBall(grid)

        assert result == [-1]

    def test3(self):
        grid = [
            [1, 1, 1, 1, 1, 1],
            [-1, -1, -1, -1, -1, -1],
            [1, 1, 1, 1, 1, 1],
            [-1, -1, -1, -1, -1, -1],
        ]
        # create an instance of the Solution class
        solution = Solution()

        # call the detectCycle function
        result = solution.findBall(grid)

        assert result == [0, 1, 2, 3, 4, -1]
