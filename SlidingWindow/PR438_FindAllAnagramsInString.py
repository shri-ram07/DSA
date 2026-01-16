class Solution(object):
    def findAnagrams(self, s, p):
        # Logic is similar to the previous problem of permutation in string
        # We will create a hashMap of the p string and then compare with every window of s string
        # If found then we will add the starting index of that window to the result list

        # Function for creating hashmap of the p and first window on s
        def createHashMap(s):
            se = {}
            for x in range(0 , len(s)):
                if s[x] not in se:
                    se[s[x]] = 1
                else:
                    se[s[x]] = se[s[x]]+1
            return se

        # creating result list and hashMap of p             
        li = []
        # creating HashMap of p
        pe = createHashMap(p)
        # left and right pointer to the window
        l , r = 0 , len(p)-1
        # creating hashMap for the First window
        se = createHashMap(s[l:r+1])
        # Iterating untill get the last element
        while r<=len(s)-1:
            # checking if window hash map is equal to the p string hash map
            if pe == se:
                li.append(l)
            # else increase the window size and and decrement the count for the lth element and if 0 theen directly remove it
            se[s[l]] = se[s[l]]-1
            if se[s[l]] == 0:
                del se[s[l]]
            # Moving the window
            l+=1
            r+=1
            # Checking for out of bound
            if r == len(s):
                break
            # checking if the new eleement not in hashMap , if not then add the key with element count
            if s[r] not in se:
                se[s[r]] = 1
            #   else increase the count
            else:
                se[s[r]] = se[s[r]]+1
            
        return li
                        
        
        
                
    
# Implimenent of class
obj = Solution()
t = obj.findAnagrams("abab" , "ab")
print(t)