class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        used = [0 for _ in range(len(nums))]

        def generate(chosen : list, user : list):
            if len(chosen) == len(nums):
                answer.append(chosen[:]) 
            for i in range(len(nums)):
                if not used[i]:
                    chosen.append(nums[i]) 
                    used[i] = 1
                    generate(chosen, used) 
                    used[i] = 0 
                    chosen.pop() 
        generate([], used) 
        return answer
