class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total = sum(arr) 
        if total%3 != 0:
            return False
        tmp = 0
        cnt = 0
        for num in arr:
            tmp += num
            if tmp == total//3:
                tmp = 0
                cnt += 1
        return cnt >= 3
