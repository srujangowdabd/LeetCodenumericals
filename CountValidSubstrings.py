class Solution(object):
    def countValidSubstrings(self, s):
        ans = 0
        first_a = -1
        a_before_b= -1
        last_bad = -1
        for i in range(len(s)):
            if s[i] == 'a' : 
                first_a = i
               
            elif s[i] == 'b' and first_a != -1:
                a_before_b = first_a
            elif s[i] =='c' and a_before_b != -1:
                last_bad = max(last_bad, a_before_b)
            ans += i - last_bad
        return ans
