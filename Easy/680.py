class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                tmp01, tmp02 = s[left:right], s[left+1:right+1] 
                return tmp01 == tmp01[::-1] or tmp02 == tmp02[::-1]
            left += 1
            right -= 1
        return True
