import copy

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        tmp = [] 
        
        def dfs(i):
            if i >= len(nums):
                answer.append(tmp.copy())
                return 
            
            tmp.append(nums[i]) 
            dfs(i+1) 
            tmp.pop() 
            dfs(i+1) 
        
        dfs(0) 
        return answer
        
