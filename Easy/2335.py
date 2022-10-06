class Solution:
    def fillCups(self, amount: List[int]) -> int:
        amount.sort(reverse=True)
        answer = 0
        while amount[0] > 0:
            if amount[1] > 0:
                amount[0] -= 1
                amount[1] -= 1
                answer += 1
            else:
                answer += amount[0] 
                amount[0] = 0
            amount.sort(reverse=True)
        return answer
