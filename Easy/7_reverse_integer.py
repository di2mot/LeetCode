class Solution:
    def reverse(self, x: int) -> int:
        if str(x)[0] != '-':
            x = int(str(x)[::-1])
        else:
            x = int('-' + str(x)[:0:-1])
        if -2**31 > x or x > 2**31:
            return 0 
        else: return x   