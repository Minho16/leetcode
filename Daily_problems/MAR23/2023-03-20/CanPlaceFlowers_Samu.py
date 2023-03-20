from typing import List
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        l = len(flowerbed)
        for i, planted in enumerate(flowerbed):
            
            if i == 0 and not planted and (l == 1 or not flowerbed[i+1]):
                n -= 1
                flowerbed[0] = 1
            elif i == l-1 and (flowerbed[i-1] == 0 or l==1) and not planted:
                n -= 1
                flowerbed[i] = 1
            elif not planted and not flowerbed[i-1] and not flowerbed[i+1]:
                n -= 1
                flowerbed[i] = 1
                
            if n == 0:
                return True
            
        return False
            

Solution().canPlaceFlowers([0],  1)
                