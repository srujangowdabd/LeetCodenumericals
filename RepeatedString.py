from math import gcd 
class Solution:
    def repeatedStringMatch(self, a: str , b: str,x: int , y : int ) -> bool:
        p , q = len(a) , len(b)
        L = q * y
        if L > p * x:
             return False 
        k = min(L , p+q - gcd(p,q))

        pattern = (b * (( k + q -1)//q))[:k]
        text = a * (( p + k - 2 ) // p + 1)

        pos = text.find(pattern)

        return pos != -1 and pos <= min(p - 1 , p* x -L)
