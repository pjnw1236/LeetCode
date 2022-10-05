class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort()
        answer = []
        x, y = 0, sum(nums)
        while True:
            if x > y:
                return answer 
            num = nums.pop()
            x += num
            y -= num
            answer.append(num)
