class Solution(object):
    def moveZeroes(self, nums):
        # Logic : We are using slow and fast pointer approach 
        # Here Slow Pointer will track the position of Zeroes
        # Fast Pointer will track the position of Non-Zeroes
        # Firstly we will check if element at slow pointer is Non-Zero then we will increment both pointers
        # If element at slow pointer is Zero then we will check element at fast pointer
        # If element at fast pointer is also Zero then we will increment fast pointer
        # If element at fast pointer is Non-Zero then we will swap both elements and increment slow pointer

        # Using Two Pointer Approach
        i , j  = 0 , 1
        # Iterating until either pointer reaches the end of the array

        while j<len(nums) and i <len(nums):
            # Checking if element at slow pointer is Non-Zero
            if nums[i] != 0:
                i+=1
                j+=1
            # If element at slow pointer is Zero
            else:
                # Checking if element at fast pointer is also Zero
                if nums[j]==0:
                    j+=1
                # If element at fast pointer is Non-Zero
                else:
                    t = nums[i]
                    nums[i] = nums[j]
                    nums[j] = t
                    i+=1
obj = Solution()
obj.moveZeroes([4,2,4,0,0,3,0,5,1,0])