class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        cumulative_sum = [0, nums[0]]
        for i in range(1, len(nums)):
            cumulative_sum.append(cumulative_sum[-1] + nums[i]) 
        
        answer = []
        for query in queries:
            for i in range(1, len(cumulative_sum)):
                if cumulative_sum[i] > query:
                    answer.append(i-1)
                    break
            else:
                answer.append(len(nums)) 
        return answer
