class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        answer = 0
        for i in range(1, len(nums)):
            if nums[i-1] >= nums[i]:
                answer += nums[i-1] - nums[i] + 1
                nums[i] = nums[i-1] + 1
        return answer
        
