class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lst = []
        freq = {}
        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        for i in range(k):
            top=max(freq, key=freq.get)
            lst.append(top)
            del freq[top]
        return(lst)
        
solution = Solution()
print(solution.topKFrequent([1,2,2,3,3,3],k=2))