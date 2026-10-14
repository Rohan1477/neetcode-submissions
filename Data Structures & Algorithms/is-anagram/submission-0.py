class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t): #this check was added so that the for loop is garunteed to go over every letter for both s and t
            return False

    #create the 26 slot aray and intilize to zero
        count = [0] * 26

        #go through each letter in both words and update array accordingly
        for i in range(len(s)):
            count[ord(s[i])- ord("a")] +=1
            count[ord(t[i])- ord("a")] -=1

        for i in range(26):
            if count[i] != 0:
                return False

        return True
        