class Solution(object):
    def lengthOfLongestSubstring(self, s):
        # I'll use the sliding window with variable lenght
        # Use two pointers to set the lenght and change the lenght of the window
        
        # I'll take a maxLen var for storing the lenght of longest substring without repeting characters
        # Move r when r is not in sub else move l untill r is not in substring 
        # store the max value of lenght in maxLen
        
        l , r = 0 , 0 
        maxLen = 0
        #Using hash for keeping track of elements counts in substring
        se = set()
        #Iterating untill r is last element
        while r < len(s):
            # if current r element not in set then add and increase r with one and chech the max value
            if s[r] not in se:
                se.add(s[r])
                r+=1
                maxLen = max(r-l , maxLen)
            #Else remove the l element and also increase l with one
            else:
                se.remove(s[l])
                l+=1
                    
        return maxLen
                
                
    
# Implimenent of class
obj = Solution()
t = obj.lengthOfLongestSubstring("pwwkeww")
print(t)