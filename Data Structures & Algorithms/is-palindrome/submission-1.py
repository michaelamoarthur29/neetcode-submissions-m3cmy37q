class Solution:
    def isPalindrome(self, s: str) -> bool:   
        newStr = '' 
    
        for char in s: 
            if char.isalnum(): 
                char.lower 
                newStr += char  
    
        reversedStr = newStr [::-1] 
    
        if reversedStr.lower() == newStr.lower(): 
            return True 
        return False 

        