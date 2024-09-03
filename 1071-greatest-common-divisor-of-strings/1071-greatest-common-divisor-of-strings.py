class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1 , len2 = len(str1) , len(str2)
        
        def valid(k):
            if len1 % k or len2 % k :
                return False
            f1,f2 = len1 // k, len2 //k
            base = str1[:k]
            return str1 == f1 * base and str2 == f2 * base
        
        for i in range(min(len1,len2),0,-1):
            if valid(i):
                return str1[:i]
        return ""   