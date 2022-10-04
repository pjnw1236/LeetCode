class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]
        cnt = 0
        for i in range(1, len(flowerbed)-1):
            if flowerbed[i-1] == 0:
                if flowerbed[i] == 0:
                    if flowerbed[i+1] == 0:
                        flowerbed[i] = 1
                        cnt += 1
        return cnt >= n
