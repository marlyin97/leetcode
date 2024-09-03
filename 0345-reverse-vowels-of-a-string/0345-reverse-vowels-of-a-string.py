class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        #strings are immutable, so converting it to list
        slist = list(s)
        
        l = 0
        r = len(slist) - 1
        
        while l < r:
            if slist[l] not in vowels:
                l += 1
                continue
            if slist[r] not in vowels:
                r -= 1
                continue
            slist[l],slist[r] = slist[r],slist[l]
            l += 1
            r -= 1
            
        return ''.join(slist)    
        
        