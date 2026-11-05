class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = []
        for i in range(len(s)):
            if s[i].isalpha() or s[i].isalnum():
                word.append(s[i].lower())
        char = ''.join(word)
        return char == char[::-1]