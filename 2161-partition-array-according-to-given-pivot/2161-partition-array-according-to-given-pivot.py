class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left = [num for num in nums if num < pivot]
        mid = [num for num in nums if num == pivot]
        right = [num for num in nums if num > pivot]
        return left + mid + right  