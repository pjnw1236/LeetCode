class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        h = int(correct[:2]) - int(current[:2]) 
        m = int(correct[3:]) - int(current[3:])
        total_minutes = 60*h + m
        times = [60, 15, 5, 1]
        total = 0
        
        for time in times:
            total += total_minutes//time
            total_minutes %=time
        
        return total
