class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d1 = dict() 
        d2 = dict() 
        answer = []
        
        for num in nums1:
            if num in d1.keys():
                d1[num] += 1
            else:
                d1[num] = 1
        
        for num in nums2:
            if num in d2.keys():
                d2[num] += 1
            else:
                d2[num] = 1
        
        for num in d1.keys():
            if num in d2.keys():
                cnt = min(d1[num], d2[num]) 
                for _ in range(cnt):
                    answer.append(num)
        
        return answer
        
        
                
        