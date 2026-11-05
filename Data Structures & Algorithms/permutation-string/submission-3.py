from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        
        sub = Counter(s1)
        for start in range(len(s2)-len(s1)+1):
            end = start+len(s1)
            if Counter(s2[start:end]) == sub:
                return True
            
        return False