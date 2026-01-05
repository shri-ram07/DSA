# This question has contraint to remove duplicate in Place 


class Solution(object):
    def removeDuplicates(self, nums):
        # Navie Approach : Using two pointers
        # Using slow and fast Pointers for checking duplicates and popping if required

        # s = 0
        # f = 0
        # Loop for iterating through the array
        # while f<len(nums):
        # Updating fast pointer
        #     f+=1
        #    # checking for end of array
        #     # If end of array is reached return length of array
        #     if f==len(nums):
        #         return len(nums)
        #     
        #     Checking if element at slow and fast pointer are equal
        #     if equal then pop the element at fast pointer and decrement fast pointer
        #     elif nums[f]==nums[s]:
        #         nums.pop(f)
        #         f-=1
        # If element at slow and fast pointer are not equal then update slow pointer to fast pointer
        #     else:
        #         s = f


        """Direct Approach : Using Dictionary key
        We can create dictionary from the list by taking them as keys
        nums_dict = dict.fromkeys(nums)
        Then we can convert the dictionary back to list
        nums = list(nums_dict.keys())
        Finally return the length of the list"""
        
         
      
            
        
    
    
obj = Solution()
arr = obj.removeDuplicates([0,0,1,1,1,2,2,3,3,4])
print(arr)