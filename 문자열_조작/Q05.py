# Q05
# 그룹 애너그램

from collections import defaultdict


def groupAnagrams(strs):
    anagrams = defaultdict(list)
    for word in strs:
        anagrams["".join(sorted(word))].append(word)
    return list(anagrams.values())


if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(groupAnagrams(strs))
    """ 
    [
        ['eat', 'tea', 'ate'], 
        ['tan', 'nat'], 
        ['bat']
    ]       
    """
