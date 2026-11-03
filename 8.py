class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Define 32-bit signed integer bounds
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        i = 0
        n = len(s)
        
        # 1. Skip leading whitespaces
        while i < n and s[i] == ' ':
            i += 1
            
        # If string is empty or contains only spaces
        if i == n:
            return 0
            
        # 2. Check for sign
        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
            
        # 3. Convert digits and handle potential overflow
        result = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            
            # Overflow check before updating result
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
                
            result = result * 10 + digit
            i += 1
            
        return sign * result
