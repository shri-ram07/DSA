from collections import deque
import collections
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        # Logic is to use deque to store the index of the elements in decreasing order
        # We will maintain the deque such that the front of the deque always has the index of the maximum element
        # We will use two pointers l and r to represent the current window

        # We will start from 0 index and move r pointer to the right if the element at r is greater than the element at the back of the deque
        # we will pop Untill the nums[r] get to its correct position in the deque
        # If the front of the deque is out of the current window we will pop it from the front
        # When the window size is equal to k we will add the front of the deque to the result array


        # arr for storing result
        arr = []
        # Two pointer for window
        l = r = 0
            # Deque for storing index of elements in decreasing order
        dq = collections.deque()
        # Start the loop untill r < len(nums)
        while r<len(nums):
            # Remove the elements which are out of this window
            while dq and dq[0] < l:
                # Pop from front
                dq.popleft()
                # Now remove all the elements smaller than the current element nums[r]
            while dq and nums[dq[-1]] < nums[r]:

                dq.pop()
            # Add the current element at the back of the deque
            dq.append(r)
            # If the window size is equal to k then add the front of the deque to the result
            if r-l+1 == k:
                arr.append(nums[dq[0]])
                # Move the left pointer to shrink the window
                l+=1
            # Move the right pointer    
            r+=1
        # Return the result array
        return arr     
    
# Implimenent of class
obj = Solution()
t = obj.maxSlidingWindow([1,3,1,2,0,5] , 3)
print(t)