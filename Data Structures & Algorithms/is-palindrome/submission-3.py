class Solution:
    def isPalindrome(self, s: str) -> bool:

        stripped_s = ""
        for i in range(len(s)):
            if s[i].isalnum():
                stripped_s += s[i].lower()
        
        s = stripped_s

        for i in range(len(s)//2):
            frt = i
            bck = len(s)-i-1
            
            if s[frt] != s[bck]:
                return False

        return True



