class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 0, num 
        while left <= right:
            mid = (left+right)//2 
            if num == mid**2:
                return True
            elif num < mid**2:
                right = mid-1
            else:
                left = mid+1
        return False 