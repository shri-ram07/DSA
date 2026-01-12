class Solution(object):
    def sortColors(self, nums):
        # The Logic is Simple , Place one pointer at last
        # Two at start named as end , mid , start respectively
        # Start -- 0   |  mid -- 1  | end -- 2
        # if you get mid as 0 then swap with start and increament
        # start and mid , if you get it equals to 2 then same with end ,do not Increament mid becuase there can be 0 then that will  be skipped
        #if you get it one then just increament mid

        # Time Complexity: O(n) where n is the length of nums
        # Space Complexity: O(1) as we are not using any extra space

        # Initialize pointers
        start , mid , end = 0 , 0 , len(nums)-1
        
        # Traverse the array until mid pointer exceeds end pointer
        while mid <= end:
            # Get the value at mid pointer
            m = nums[mid]
            # Check the value and perform corresponding actions
            if m == 0:
                # Swap values at start and mid pointers
                nums[start] , nums[mid] = nums[mid] , nums[start]
                # Increment start and mid pointers
                start+=1
                mid+=1
            # If value is 1, just increment mid pointer
            elif m == 1 :
                mid+=1
            # If value is 2, swap values at mid and end pointers and decrement end pointer
            # Do not increment mid pointer here
            # because the swapped value needs to be checked
            # again , it can be 0 ,1 or 2
            else:
                nums[mid] , nums[end] = nums[end] , nums[mid]
                end-=1
      
            
            
            
                
            
            
        
    

# Implimenent of class
obj = Solution()
obj.sortColors([1,2,0])