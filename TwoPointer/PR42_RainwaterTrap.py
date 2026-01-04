class Solution(object):
    # The Universal Approach of solving this questions is to find the water stored by specific point will be equal to
    # min(lmax , rmax) - height[i]
    # where lmax is the maximum height to the left of that point and rmax is the maximum height to the right of that point.
    # [Time Complexity]: O(N)
    # [Space Complexity]: O(1)

    # We can do this by two methods : 
    # 1. Using two auxiliary arrays to store lmax and rmax for each point.
    # 2. Using two pointers to keep track of lmax and rmax while traversing the array from both ends.
    def trap(self, height):
            """# Method 1
            # First Approach will be maintaing two auxiallary arrays , lmax and rmax
            rmaxx = height[len(height)-1]
            lmaxx = height[0]
            water = 0
            # Auxiliary arrays
            rmax = []
            lmax = []
            # Filling lmax and rmax arrays
            # This loop fills lmax array in such a way that lmax[i] contains the maximum height to the left of index i
            for i in range(len(height)):
                if height[i] > lmaxx:
                    lmaxx = height[i]
                    lmax.append(lmaxx)
                    
                else:
                    lmax.append(lmaxx)
            # This loop fills rmax array in such a way that rmax[i] contains the maximum height to the right of index i       
            for j in range(len(height)-1, -1 , -1):
                if height[j] > rmaxx:
                    rmaxx = height[j]
                    rmax.append(rmaxx)
                    
                else:
                    rmax.append(rmaxx)
            # Reversing rmax array to align it with the original height array
            rmax.reverse()
            # Calculating the total water trapped
            for k in range(len(height)-1):
                water += (min(lmax[k] , rmax[k]))-height[k]
            
            
            return water"""
            # Method 2
            # Using two pointers to keep track of lmax and rmax
            # Initialize two pointers at the start and end of the array
            l , r = 0 , len(height)-1
            # Initialize lmax and rmax to keep track of maximum heights from both ends
            lmax , rmax = 0 , 0
            # Initialize variable to store total water trapped
            water = 0
            # Traverse the array until the two pointers meet
            while l<r:
                # calculate lmax and rmax in such a way that it hold max value till that point
                lmax = max(lmax , height[l])
                rmax = max(rmax , height[r])

                # If lmax is less than rmax, then the water trapped at index l is determined by lmax
                if lmax<rmax:
                    water+= lmax - height[l]
                    l+=1
                # If rmax is less than or equal to lmax, then the water trapped at index r is determined by rmax
                else:
                    water+=rmax - height[r]
                    r-=1
            
            return water
        
obj = Solution()
area = obj.trap([0,1,0,2,1,0,1,3,2,1,2,1])
print(area)