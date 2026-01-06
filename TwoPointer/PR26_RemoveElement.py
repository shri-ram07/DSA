class Solution(object):
    def removeElement(self, nums, val):
        # Logic: We are comparing each element with the given value
        # If element is equal to the value then we are replacing that element with the last element of the array
        # reuducing the value of j pointer by 1
        # If element is not equal to the value then we are just incrementing the i pointer


        # Using two pointers  approach
        i , j = 0 , len(nums)


        while i<j:
            # Checking if element at i pointer is equal to the given value
            if nums[i] == val:
                # If equal then replacing that element with last element of the array
                nums[i] = nums[j-1]
                # reducing the value of j pointer by 1
                j-=1
            # If element is not equal to the value then we are just incrementing the i pointer
            else:
                i+=1
                
        return i
        
                
      
            
        
    
    
obj = Solution()
arr = obj.removeElement([2],3)
print(arr)