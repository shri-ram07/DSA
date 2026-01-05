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
        # best Approach : Using these two pointers , slow and fast , just checking for all unique 
        # values and placing them to index of slow pointer
        # and increamenting the slow pointer only when unique value is found

        # Initialising slow pointer
        k = 1
        if len(nums)!=1:
            # Iterating through the array from index 1 to end
            # 
            for i in range(1,len(nums)):
                # Checking if current element is not equal to previous element
                if nums[i] != nums[i-1]:
                    # If not equal then placing the current element at index of slow pointer
                    nums[k] = nums[i]
                    #increamenting slow pointer
                    k+=1
        
        return k


      
            
        
    
    
obj = Solution()
arr = obj.removeDuplicates([0,0,1,1,1,2,2,3,3,4])
print(arr)