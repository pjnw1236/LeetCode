# Q01
# 유효한 팰린드롬

from collections import deque


def isPalindrome(s):
    # 문자열 s가 주어질때, s의 원소 중에서 대소문자 및 숫자만 strs deque에 저장
    strs = deque()
    for char in s:
        # 영어대소문자일 경우 strs 리스트에 소문자로 변환 후 저장
        if char.isalpha():
            strs.append(char.lower())
        # 숫자일 경우 strs 리스트에 그대로 저장
        elif char.isdigit():
            strs.append(char)

    # strs deque에서 가장 좌측에 있는 원소와 가장 우측에 있는 원소를 꺼내 다르다면, False 반환
    # False가 아닌 경우 True 반환
    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False
    return True


if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    print(isPalindrome(s))  # True
    s = "race a car"
    print(isPalindrome(s))  # False
