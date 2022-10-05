class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x : -x[1]) 
        answer = 0

        for boxType in boxTypes:
            if truckSize >= boxType[0]:
                truckSize -= boxType[0]
                answer += boxType[0] * boxType[1]
            else:
                answer += truckSize * boxType[1] 
                truckSize = 0 
            if truckSize == 0:
                return answer
        return answer
