class Solution:
    def minimumSum(self, num: int) -> int:
        nums = [int(i) for i in str(num)]
        nums.sort() 
        answer = 10*(nums[0] + nums[1]) + nums[2] + nums[3]
        return answer
