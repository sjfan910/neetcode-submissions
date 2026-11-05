from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        
        sub = Counter(s1)
        start = 0
        end = start+len(s1)
        window = dict(Counter(s2[start:end]))
        for start in range(len(s2)-len(s1)+1):
            end = start+len(s1)
            if window == dict(sub):
                return True
            if end == len(s2):
                break
            if window.get(s2[start]) == 1:
                del window[s2[start]]
            else:
                window[s2[start]] -= 1
            window[s2[end]] = window.get(s2[end],0) + 1
            
        return False
            
        return False