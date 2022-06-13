# Q02
# 문자열 뒤집기

def reverseString(s):
    left = 0
    right = len(s) - 1
    # left와 right 서로 값 변경
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s

# def reverseString(s):
#     s.reverse()
#     return s


if __name__ == "__main__":
    s = list("abc")  # ["a", "b", "c"]
    print(reverseString(s))  # ["c", "b", "a"]
