class Solution(object):
    def characterReplacement(self, s, k):
        # We will use sliding window approach
        # We just have to return the lenght of longest substring in which 
        # we can replace maximum K char to any alph. to make a longest 
        # substring with all same charcters, and we have to return the lenght
        # So the problem is not about replacing characters , 
        # its about returning the lenght which we will store in maxWin
        # We have to create a hash map or dictonary to store the frequency of all elements 
        # and the formual for knowing how many characters we can replace from a window 
        # is charsToreplac = windowSize - maxFrequncy from hash map
        # and it should be smaller than k else we have to reduce the size of the window
        # we will use two pointer approach for window size flexibility
        
        # Two pointer left and right
        l , r = 0 , 0
        # variable for storing maximum window size
        maxWind = 0
        # Hash map in the form of dictionary
        hashMap = {}
        maxFreq = 0
        # Taking Window to compare each time
        win = 1
        #Iterating Untill get to last index
        while r<len(s):
            
            # if the current char key is not in the hash Map then put the key and value to 1
            if s[r] not in hashMap:
                hashMap[s[r]] = 1
            # If present then just increment
            elif s[r] in hashMap:
                hashMap[s[r]] = hashMap[s[r]]+1
            #Calculate the maximum frequency of any element because we will replace the element with lowest frequency so we can substract from the 
            # current window to get the number of element that is lesser frequency and compare with the k to check the replacement validity
            maxFreq = max(hashMap[s[r]] , maxFreq)
            
            # checking th requirement for replacement 
            charsToReplace = win - maxFreq
            if charsToReplace <= k:
                # if found then updATE the max 
                maxWind = max(maxWind , win)
                
            #else decrease the window size and remove the 1 count of l element
                
            else:
                win-=1
                hashMap[s[l]] = hashMap[s[l]]-1
                l+=1
                
            #Increment the window size and r index
            win+=1
            r+=1
            
        return maxWind



# Implimenent of class
obj = Solution()
t = obj.characterReplacement("AAAAAAA" , 1)
print(t)