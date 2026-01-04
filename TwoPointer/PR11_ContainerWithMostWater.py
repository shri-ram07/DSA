class Solution(object):
    def maxArea(self, height):
        # Initialize two pointers at the start and end of the array
        x , y = 0 , len(height)-1
        # Initialize variable to store maximum volume
        vol = 0
        while x!=y:

            # Area = Height of shorter line * distance between two lines
            # After Calculating the area move the pointer which is at the shorter line towards the other pointer

            # There will be hence two conditions to move the pointers
            # 1. If height at left pointer is less than or equal to height at right
            # 2. If height at right pointer is less than height at left

            if height[x]>=height[y]:
                area = height[y]*(y-x)
                # Move the right pointer towards left
                y-=1
            elif height[y]>=height[x]:
                area = height[x]*(y-x)
                # Move the left pointer towards right
                x+=1
            # Update the maximum volume if current area is greater than previous maximum volume
            if area>vol:
                vol = area
        return vol
        
        
obj = Solution()
area = obj.maxArea([1,8,6,2,5,4,8,3,7])
print(area)