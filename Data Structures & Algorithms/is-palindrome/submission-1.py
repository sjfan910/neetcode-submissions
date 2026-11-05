class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ''
        for i in range(len(s)):
            if s[i].isalpha() or s[i].isalnum():
                word += s[i].lower()
        return word == word[::-1]