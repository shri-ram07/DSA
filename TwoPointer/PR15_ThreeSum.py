class Solution(object):
    def threeSum(self, nums):
        # I will use the two pointer approach
        # after sorting the array to find
        # triplets that sum to zero.
        # [Time Complexity]: O(N^2)

        # I'll fix one pointer and use two pointers on remaining section and 
        # I will move the first pointer after checking all the pairs for that fixed pointer.

        nums.sort()
        res = []
        for i in range(len(nums)-2):
            y = i+1
            z = len(nums)-1

            while y < z:
                sum = nums[i]+nums[y]+nums[z]
                if sum == 0:
                    if [nums[i] , nums[y] , nums[z]] in res:
                        z-=1
                        y+=1
                        continue
                    res.append([nums[i] , nums[y] , nums[z]])
                    z-=1
                    y+=1
                elif sum > 0:
                    z-=1
                elif sum < 0:
                    y+=1

        return res






obj = Solution()
res = obj.threeSum([-1,0,1,2,-1,-4])
print(res)