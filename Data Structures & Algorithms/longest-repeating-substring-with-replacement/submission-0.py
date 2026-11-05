class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        output = 0
        l,r = 0,0
        while r<len(s):
            if s[r] not in freq:
                freq[s[r]] = 1
            else:
                freq[s[r]] += 1
                
            highest = max(freq, key=lambda k: freq[k])
            
            if r-l+1 - freq[highest] <= k:
                output = max(r-l+1, output)
            else:
                if freq[s[l]] != 1:
                    freq[s[l]]-=1
                else:
                    del freq[s[l]]
                l += 1
            r += 1
        return output