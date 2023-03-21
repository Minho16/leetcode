class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        if n == 0:
            return True

        available_plots = 0

        counter = 1 if not flowerbed[0] else 0

        for i in flowerbed:
            if i:
                if counter >= 3:
                    available_plots += (counter - 1) // 2
                counter = 0
            else:
                counter += 1

        if flowerbed[-1] == 0:
            counter += 1
            if counter >= 3:
                available_plots += (counter - 1) // 2

        return True if available_plots >= n else False
