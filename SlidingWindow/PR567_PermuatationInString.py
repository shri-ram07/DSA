class Solution(object):
    
    def checkInclusion(self, s1, s2):
        # Use the fixed sliding window approach 
        # where the lenght of the window will be equal to the lenght of s1
        # We will Create a hashMap with char count of the s1 then compare with hashMap of every window
        # if found then retrun True else move the window 1 step
        # and decrement one count of lth element and if 0 then delete that key
        
        # Function for creating hashmap of the s1 and first window on s2
        def createHashMap(s):
            se = {}
            for x in range(0 , len(s)):
                if s[x] not in se:
                    se[s[x]] = 1
                else:
                    se[s[x]] = se[s[x]]+1
            return se
                    
            
        #creating HashMap of s1
        ma = createHashMap(s1)
        # left and right pointer to the window
        r = len(s1)-1
        l = 0
        # creating hashMap for the First window
        hashMap = createHashMap(s2[0:r])
        # Iterating untill get the last element
        while r<len(s2):
            # checking if the new eleement not in hashMap , if not then add the key with element count
            if s2[r] not in hashMap:
                hashMap[s2[r]] = 1
            else:
                hashMap[s2[r]] = hashMap[s2[r]]+1
                
            #checking if window hash map is equal to the string hash map
            if ma == hashMap:
                return True
            
            # else increase the window size and and decrement the count for the lth element and if 0 theen directly remove it 
            else:
                r+=1
                hashMap[s2[l]] = hashMap[s2[l]]-1
                if hashMap[s2[l]] == 0:
                    del hashMap[s2[l]]
                
                l+=1
        return False
                
                
    
# Implimenent of class
obj = Solution()
t = obj.checkInclusion("ab" , "eidbaooo")
print(t)