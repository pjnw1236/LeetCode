# Q06
# 가장 긴 팰린드롬 부분 문자열

def longestPalindrome(s):
    def expand(left, right):
        while left >= 0 and right <= len(s)-1 and s[left] == s[right]:
            left -= 1
            right += 1
        # while문 종료 후에는 s[left] != s[right]이므로 left+1:right 인덱스까지의 값 반환
        return s[left+1:right]
    if len(s) < 2 or s == s[::-1]:
        return s
    # result : 가장 긴 팰린드롬 저장
    result = ""
    for i in range(len(s)-1):
        # expand(i, i+1) : 팰린드롬 원소가 짝수개인 경우
        # expand(i, i+2) : 팰린드롬 원소가 홀수개인 경우
        result = max(result, expand(i, i+1), expand(i, i+2), key=len)
    return result


if __name__ == "__main__":
    s = "babad"
    print(longestPalindrome(s))  # "bab"
    s = "cbbd"
    print(longestPalindrome(s))  # "bb"
