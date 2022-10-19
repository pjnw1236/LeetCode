class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = dict() 
        for word in words:
            if word in d.keys():
                d[word] += 1
            else:
                d[word] = 1
        answer = sorted(d, key = lambda x : (-d[x], x))
        return answer[:k]
        
        