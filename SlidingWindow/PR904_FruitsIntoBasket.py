class Solution(object):
    def totalFruit(self, fruits):
        # Logic is to use sliding window approach
        # We will use two pointers l and r to represent the current window
        # We will move the r pointer to the right and keep adding the fruits to the basket
        # When the number of unique fruits in the basket exceeds 2 we will move the l pointer to the right or shrink the window
        # We will keep track of the largest window size which has at most 2 unique fruits
        # Finally we will return the largest window size
        # Initialize two pointers l
        l =  0
        # Initialize result to store the largest window size
        res = 0
        # Initialize a dictionary to store the count of each fruit in the current window
        s = {}
        # Start the loop for r pointer
        for r in range(len(fruits)):
            # Add the current fruit to the basket
            if fruits[r] not in s:
                # If fruit not in basket add it with count 1
                s[fruits[r]] = 1
            # If fruit already in basket increment its count
            else:
                # Increment the count of the fruit
                s[fruits[r]]+=1
            # Shrink the window until the number of unique fruits is less than or equal to 2
            while len(s)>2:
                # Shrink the window from the left
                s[fruits[l]]-=1
                # If the count of the fruit becomes 0 remove it from the basket
                if s[fruits[l]] == 0:
                    # Remove the fruit from the basket
                    del s[fruits[l]]  
                    # Move the left pointer to the right
                # Move the left pointer to the right
                l+=1
            # Update the largest window size
            else:
                # Update the result with the maximum size of the window
                res = max(res , r-l+1)
            # Move the right pointer to the right
            r+=1
        # Return the largest window size
        
        return res
            
        
        
        
o = Solution()
a = o.totalFruit([3,3,3,1,2,1,1,2,3,3,4])
print(a)