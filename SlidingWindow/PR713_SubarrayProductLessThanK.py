class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        # Logic : Use sliding window
        # Multiply each element one by one and increase
        # thw window lenght and when we get and mul value greater than or equal to  k 
        # then start shrinking the window and  divide the mul with nums[l] to remove the element and move l to right untill it is smaller than r , else break
        # Here to track the count of sub array we need a little more logic
        # If multiplication untill current nums[r] is smaller than k then total number of subarray possible will be r-l+1
        # beacause lets assume a case 
        # [1 , 2, 3, 4]   k = 30 and when l = 0  and r = 3 , it is less than 3-
        #  |         |
        # Total Number of subaraay will be 4 as per formula
        # [1,2,3,4] , [2,3,4] , [3,4] , [4]
        
        
        # l pointer for left tracking
        l = 0
        # le to store max windows counts
        le = 0
        # mul to track multiplications
        mul = 1
        # Start the loop for right pointer
        for r in range(len(nums)):
            # calculate the multiplication
            mul*=nums[r]
            # check if multiplication is greater than or equal to k , and if not then make by shrinking
            while mul>=k:
                # check if l is less than r or not
                if l < r:   
                    # if yes then divide the mul with nums[l] to remove the element nums[l] from mul contributions
                    mul = mul/nums[l]
                    # Update the l
                    l+=1
                # break if l is equals to r
                else:
                    break
            # if mul is less than k then add the sub arrays
            else:
                le+=(r-l+1)
        return le
        
        
        
o = Solution()
a = o.numSubarrayProductLessThanK([1,2,3,4,5] ,1)
print(a)