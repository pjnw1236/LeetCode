# Q04
# 가장 흔한 단어

import re
from collections import Counter

# paragraph : 문자열
# banned : 금지된 단어 목록


def mostCommonWord(paragraph, banned):
    # 정규표현식에 접미사 r을 붙이면 이스케이프 하지 않고 문자 그대로 해석이됨 (raw string)
    # [^\w] : 문자와 숫자가 아닌 것을 의미하며, 문자와 숫자가 아닌 것을 " "로 치환
    words = [word for word in re.sub(
        r"[^\w]", " ", paragraph).lower().split() if word not in banned]
    counts = Counter(words)
    # most_common(n) : 가장 빈도가 높은 순서대로 n개의 원소 반환
    return counts.most_common(1)[0][0]


if __name__ == "__main__":
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    print(mostCommonWord(paragraph, banned))  # "ball"
    # counts = Counter({'ball': 2, 'bob': 1, 'a': 1, 'the': 1, 'flew': 1, 'far': 1, 'after': 1, 'it': 1, 'was': 1})
    # counts.most_common(1) = [("ball", 2)]
