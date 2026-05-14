class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        cleaned = ""

        for word in s:
            if word.isalnum():
                cleaned += word.lower()
        
        
        
        rev = ""

        for char in cleaned:
            rev= char + rev

        return cleaned == rev

        