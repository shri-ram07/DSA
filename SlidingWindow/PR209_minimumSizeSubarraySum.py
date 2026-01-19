class Solution(object):
    def minSubArrayLen(self,target, nums):
        # Logic is to use sliding window approach
        # We will use two pointers l and r to represent the current window
        # We will move the r pointer to the right and keep adding the elements to the sum
        # When the sum is greater than or equal to target we will move the l pointer to the right or shrink the window
        # We will keep track of the smallest window size which has sum greater than or equal to target
        # Finally we will return the smallest window size
        # If no such window exists we will return 0 #
        # Initialize two pointers l 
        l = 0 
        # Initialize sum and smallest window size
        sum_ = 0
        # Initialize smallest window size to infinity
        smallest = float("inf")
        # Start the loop for r pointer
        for r in range(len(nums)):
            # Add the current element to the sum
            sum_+=nums[r]
            # Shrink the window until the sum is less than target
            while sum_>=target:
                # Update the smallest window size
                smallest = min(r-l+1 , smallest)
                # Shrink the window from the left
                sum_-=nums[l]
                # Move the left pointer to the right
                l+=1
                # Move the right pointer to the right
            r+=1
        # Return the smallest window size
        return smallest if smallest!= float("inf") else 0