class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        remain = [0, 0]
        for bill in bills:
            if bill == 5:
                remain[0] += 1
            elif bill == 10:
                if remain[0] > 0:
                    remain[0] -= 1
                    remain[1] += 1
                else:
                    return False
            else:
                if remain[0] > 0 and remain[1] > 0:
                    remain[0] -= 1
                    remain[1] -= 1
                elif remain[0] >= 3:
                    remain[0] -= 3
                else:
                    return False 
        return True
