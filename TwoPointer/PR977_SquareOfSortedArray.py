class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """# Simple approach: Square each element and sort the array
        # Time Complexity: O(n log n)
        # Space Complexity: O(n)
        nums = [x*x for x in nums]
        nums.sort()
        return nums"""
      
        # Optimal approach: Two pointer approach
        # Find the partition point where negative numbers end and non-negative numbers start
        # Then merge the squares of negative and non-negative parts
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        
        l , r = 0 , 0
        # Check if all elements are non-negative
        # If yes, return the squares of the elements as they are already sorted
        if (nums[r] >= 0 and nums[l] >=0):
                return [x*x for x in nums]
        
        # Find the partition point
        while r<len(nums):
            if nums[r]<0 and nums[l]<0:
                r+=1
            else:
                break
        # Split the array into negative and non-negative parts
        # arr1 will hold the negative part in reverse order
        arr1 = nums[0:r][::-1]
        # arr2 will hold the non-negative part
        arr2 = nums[r:len(nums)]
        
        l1 = len(arr1)
        l2 = len(arr2)
        
        r = 0
        # res will hold the final sorted squares 
        res = []

        # Merge the squares of arr1 and arr2
        while l<l1 and r<l2:
            el1 = abs(arr1[l])
            el2 = arr2[r]
            if el1<el2:
                res.append(el1*el1)
                l+=1
            else:
                res.append(el2*el2)
                r+=1
        # If there are remaining elements in arr1
        while l<l1:
            res.append(abs(arr1[l])*abs(arr1[l]))
            l+=1
        # If there are remaining elements in arr2
        while r<l2:
            res.append(arr2[r]*arr2[r])
            r+=1

            
        
                    
                
        return res
    



    

# Implimenent of class
obj = Solution()
print(obj.sortedSquares([-4,-1,0,3,10]))  # Output: [0,1,9,16,100]