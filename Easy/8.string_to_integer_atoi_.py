class Solution:
    def myAtoi(self, s: str) -> int:

        s = s.strip()
        res = ''
        flag = False
        max_int = 2_147_483_647
        min_int = -2_147_483_648
        
        for i in range(len(s)):
            if s[i].isdigit() or s[i] in ('+', '-'):

                if flag:
                    if s[i] in ('+', '-'):
                        break
                flag = True
                res += s[i]
            else: break
 
        if not flag: return 0

        if len(res) == 1:
            if res in ('+', '-'): return 0
            else: return int(res)
        if (int(res) >= min_int) and (int(res) <= max_int):
            return int(res)
        elif int(res) < min_int: return min_int
        elif int(res) > max_int: return max_int
        return 0
    
e = "+-12"
s = Solution()
b = s.myAtoi(e)
print(b)

'''
Runtime: 62 ms, faster than 5.11% of Python3 online submissions for String to Integer (atoi).
Memory Usage: 14.2 MB, less than 83.06% of Python3 online submissions for String to Integer (atoi).
'''