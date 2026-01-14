class Solution(object):
    def lengthOfLongestSubstring(self, s):
        # Using Sliding Window Approach
        # l and r are two pointers
        # se is a set to store unique characters
        # Logic : If character at r pointer is not in set, add it to set and move r pointer to right
        # If character at r pointer is in set, remove character at l pointer and move l pointer to right


        le = 0
        se = set()
        l , r = 0 , 0
        # Iterate until r pointer reaches end of string
        while r<=len(s)-1:
            # If character at r pointer is not in set
            if s[r] not in se:
                # Add character at r pointer to set
                se.add(s[r])
                # Move r pointer to right
                r+=1
                # Update length of longest substring
                le = max(len(se) , le)
            # If character at r pointer is in set
            else :
                # Remove character at l pointer and move l pointer to right
                # Check if l is less than r to avoid index error

                if l<r:
                    se.remove(s[l])
                    l+=1
                
                # If l is equal to r, move both pointers to right
                else:
                    se.remove(s[l])
                    l+=1
                    r+=1
        return le
                    
            
        
            
# Implimenent of class
obj = Solution()
t = obj.lengthOfLongestSubstring("a")
print(t)