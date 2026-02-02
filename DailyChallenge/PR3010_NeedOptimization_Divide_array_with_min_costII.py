class Solution(object):
    def minimumCost(self, nums, k, dist):
        if len(nums)<=1:
          return nums[0]
        res = float("inf")
        l , r = 1 , dist+1
        arr = nums[l:r+1]
        while r<len(nums):
          
          score = nums[0]
          arr2 = sorted(arr)
          score = score+sum(arr2[:k-1])
          res = min(score , res)
          del arr[0]
          if not r == len(nums)-1:
            arr.append(nums[r+1])
          l+=1
          r+=1
        return res
        
        
        
o = Solution()
a = o.minimumCost([1,3,2,6,4,2] , 3 , 3 )
print(a)