class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        cleaned_s = ""
        for c in s:
            if c.isalnum():
                cleaned_s += c
        reversed = cleaned_s[::-1]
        return (cleaned_s == reversed)
