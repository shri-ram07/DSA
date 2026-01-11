class Solution(object):
    def backspaceCompare(self, s, t):
        # Using Stack Approach
        # Time Complexity: O(n + m) where n and m are lengths of s and t
        # Space Complexity: O(n + m)
        # we will traverse both strings , if we encounter a character other than '#', we push it onto the stack
        # if we encounter '#', we pop the top character from the stack if it's not empty

        # First string Processing
        r = 0
        # Processed string for s
        s_ = ""
        
        while r<len(s):
            # If current character is not '#', append it to s_
            if s[r] != "#":
                s_+=s[r]
                r+=1
            # If current character is '#', remove the last character from s_ if it's not empty
            else:
                s_ = s_[:-1]
                r+=1
        
        r = 0
        # Processed string for t
        t_=""
        while r<len(t):
            # If current character is not '#', append it to t_
            if t[r] != "#":
                t_+=t[r]
                r+=1
            # If current character is '#', remove the last character from t_ if it's not empty
            else:
                t_ = t_[:-1]
                r+=1
        # Compare the processed strings and return the result
        return s_== t_

# Implimenent of class
obj = Solution()
obj.backspaceCompare("ab##" , "cd#") 
