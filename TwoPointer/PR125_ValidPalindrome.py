class Solution(object):
    def isPalindrome(self, s):

            # Logic : We are using two pointer approach
            # Here Left Pointer will start from beginning of string
            # Right Pointer will start from end of string
            # We will check if both characters at left and right pointer are Alphanumeric
            # If both characters are Alphanumeric then we will compare them
            # If they are equal then we will increment left pointer and decrement right pointer

            
            l , r = 0 , len(s)-1
            # Converting the string to Lowercase
            s = s.lower()
            # Iterating until left pointer is less than or equal to right pointer
            while l<=r:
                # Checking if both characters at left and right pointer are Alphanumeric
                if not s[l].isalnum():
                    l+=1
                # Checking if character at right pointer is not Alphanumeric
                elif not s[r].isalnum():
                    r-=1
                # If both characters are Alphanumeric
                else :
                    # Comparing both characters
                    if s[l] != s[r]:
                        # If characters are not equal then return False
                    
                        return False
                    # If characters are equal then increment left pointer and decrement right pointer
                    else:
                        l+=1
                        r-=1
                
            return True
                    
            
            
        

        
                
      
            
        
    
    
obj = Solution()
a = obj.isPalindrome("A man, a plan, a canal: Panama")
print(a)

