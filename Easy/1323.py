class Solution:
    def maximum69Number (self, num: int) -> int:
        num_lst=[i for i in str(num)]
        for i in range(len(str(num))):
            if num_lst[i] != "9":
                num_lst[i] = "9"
                break 
        return int("".join(num_lst))
