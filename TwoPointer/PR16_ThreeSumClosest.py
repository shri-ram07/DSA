class Solution(object):
    def threeSumClosest(self, nums, target):
        # Sort The array
        # Fix one pointer and use two pointers to find the closest sum
        # We have to return the sum which is closest to target
        
        closest_sum = nums[0] + nums[1] + nums[2]
        closest_sum_diff = max(nums)+10**100

        nums.sort()
        for i in range(len(nums)-2):
            print("Loop started")
            x , y = i+1 , len(nums)-1
            while x<y:
                # Do same as 3 sum to fins the sum equals to target 
                # if found then return directly and update the two pionters accordingly

                sum = nums[i] + nums[x] + nums[y]
                print("Sum  is ", sum)
                if sum == target:
                    return sum
                elif sum < target:
                    x+=1
                elif sum > target:
                    y-=1
                
                # Main Crux to find the closest sum
                # Here we will check if the current sum is closer to target than the previous closest sum
                # If yes then we will update the closest sum
                
                closest_sum_diff_current = abs(sum-target)
                if closest_sum_diff > closest_sum_diff_current:
                    print("Closest Sum is", closest_sum)
                    closest_sum = sum
                    closest_sum_diff = closest_sum_diff_current
                    
                
                
        return closest_sum
        





obj = Solution()
res = obj.threeSumClosest([1,1,1,0], -100)
print(res)