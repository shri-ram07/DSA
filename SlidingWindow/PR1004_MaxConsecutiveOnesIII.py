class Solution(object):
    def longestOnes(self, nums, k):
        # use the sliding window approach
        # Create a cnt var to store the count of 0's
        # if the count increases to k then we will shrink the window untill it get to k
        # and then we will continue the increment the window
        
        # left Pointer
        l = 0
        # Counter to store the value of count of zeros
        cnt = 0
        # le top store the length of the max window
        le = 0
        # start the loop
        for r in range(len(nums)):
            # check if curretn element is zero then increment the cnt
            if nums[r] == 0:
                cnt+=1
            # increment l untill cnt > k and remove if found zero
            while cnt > k:
                # shrink the window untill we find the optimal lenght 
                if nums[l] == 0:
                    cnt-=1
                l+=1
            # find the max lenght
            le = max(le , r-l+1)
            # Update the r
            r+=1
        return le
        
        
        
o = Solution()
a = o.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1] , 4)
print(a)