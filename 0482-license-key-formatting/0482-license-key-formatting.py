import math
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        sample = ''.join(s.split('-'))
        n = len(sample)
        #print(sample)
        new_s = sample[:(n%k)]  
        sample = sample[(n%k):]  
        if new_s:
            new_s += '-'
        #print(new_s)
        for i in range(n//k):
            new_s += sample[i*k : i * k + k ]
            new_s += '-'
            #print(new_s)
        result = ''.join(new_s[:-1])
        #print(result)
        chars = [char if char.isupper() else char.upper() for char in result ]
        #print(chars)
        return ''.join(chars)



             

       